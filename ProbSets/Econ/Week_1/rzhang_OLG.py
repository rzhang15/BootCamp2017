import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib.ticker import MultipleLocator
import os

# Answers are at the bottom of the file

# Firm's Parameters
labor = np.array([1,1,0.2])
delta = 0.6415
alpha = 0.35
# Household Parameters
periods = 3
beta = 0.442
sigma = 3.0
A = 1.0
# Time Path parameters
T = 10*periods
TPI_tol = 1e-9
xi = 0.15

def get_r(K, L, alpha, A, delta):
    return alpha*A*(L/K)**(1-alpha)-delta

def get_w(K, L, alpha, A):
    return (1-alpha)*A*((K/L)**alpha)

def get_c(b2, b3, r, w):
    return (1+r)*b2+w-b3

def get_MU(c, sigma):
    epsilon = 0.0001
    if c < epsilon:
        b2 = (-sigma*(epsilon**(-sigma-1)))/2
        b1 = (epsilon**(-sigma))-2*b2*epsilon
        return 2*b2*c+b1
    else:
        return c**(-sigma)

def EulErr(bvec, *args):
    delta, alpha, beta, sigma, A, l1, l2, l3, r2, r3, w1, w2, w3 = args
    b2 = bvec[0]
    b3 = bvec[1]
    if r2 == -1 and w1 == -1:
        K = b2+b3
        L = l1+l2+l3
        r2 = get_r(K, L, alpha, A, delta)
        r3 = r2
        w1 = get_w(K, L, alpha, A)
        w2 = w1
        w3 = w1
    MU_c1 = get_MU(get_c(0, b2, 0, l1*w1), sigma)
    MU_c2 = get_MU(get_c(b2, b3, r2, l2*w2), sigma)
    MU_c3 = get_MU(get_c(b3, 0, r3, l3*w3), sigma)
    err1 = MU_c1 - beta*(1+r2)*MU_c2
    err2 = MU_c2 - beta*(1+r3)*MU_c3
    err_vec = np.array([err1, err2])
    return err_vec

def SS_OLG(b_args, b2_init, b3_init, labor):
    delta, alpha, beta, sigma, A = b_args
    b_init = np.array([b2_init, b3_init])
    eul_args = (delta, alpha, beta, sigma, A, labor[0], labor[1], labor[2], -1, -1, -1, -1, -1)
    b_result = opt.root(EulErr, b_init, args=(eul_args))
    b2 = b_result.x[0]
    b3 = b_result.x[1]
    K = b2+b3
    L = np.sum(labor)
    w = get_w(K, L, alpha, A)
    r = get_r(K, L, alpha, A, delta)
    c_result = np.array([get_c(0, b2, 0, labor[0]*w), get_c(b2, b3, r, labor[1]*w), get_c(b3, 0, r, labor[2]*w)])
    print(b_result)
    print('Savings: ', b_result.x)
    print('Consumption: ', c_result)
    print('Wage: ', w)
    print('Interest: ', r, '\n')
    return b_result.x

def get_K(b_init, b_args, b_SS, labor):
    delta, alpha, beta, sigma, A, T, TPI_tol, xi = tpi_args
    L = np.sum(labor)
    Kvec = np.linspace(np.sum(b_init), np.sum(b_SS), T)
    err = 100
    iteration = 0
    while err > TPI_tol:
        r0 = get_r(Kvec[0], L, alpha, A, delta)
        r1 = get_r(Kvec[1], L, alpha, A, delta)
        w0 = get_w(Kvec[0], L, alpha, A)
        w1 = get_w(Kvec[1], L, alpha, A)

        b2vec = b_init[0]*np.ones(T)
        b3vec = b_init[1]*np.ones(T)

        b3_args = (beta, sigma, w0, w1, r0, r1, b2vec[0], labor[1], labor[2])
        b_32init = 0.02
        b3vec[1] = opt.root(get_b32, b_32init, args=(b3_args)).x[0]

        for i in range(1, T-1):
            l1 = labor[0]
            l2 = labor[1]
            l3 = labor[2]
            w1 = get_w(Kvec[i-1], L, alpha, A)
            w2 = get_w(Kvec[i], L, alpha, A)
            w3 = get_w(Kvec[i+1], L, alpha, A)
            r2 = get_r(Kvec[i], L, alpha, A, delta)
            r3 = get_r(Kvec[i+1], L, alpha, A, delta)
            pass_args = (delta, alpha, beta, sigma, A, l1, l2, l3, r2, r3, w1, w2, w3)
            b_result = opt.root(EulErr, b_init, args=(pass_args))
            b2vec[i] = b_result.x[0]
            b3vec[i+1] = b_result.x[1]

        b2vec[T-1] = b2vec[T-2]

        iteration = iteration+1

        Knew = b2vec + b3vec
        Kdiff = np.square(Kvec-Knew)
        err = sqrt(np.sum(Kdiff))
        print('Iteration:', iteration, ' Error:', err)
        Kvec = xi*Knew + (1-xi)*Kvec
    return Kvec

def get_b32(b32, *args):
    beta, sigma, w1, w2, r1, r2, b21, l2, l3 = args
    MU1 = get_MU(get_c(b21, b32, r1, l2*w1), sigma)
    MU2 = get_MU(get_c(b32, 0, r2, l3*w2), sigma)
    return MU1-beta*(1+r2)*MU2

b2_init = 0.02
b3_init = 0.02

#Problem 1
b_args = (delta, alpha, beta, sigma, A)
print('Problem 1')
result1 = SS_OLG(b_args, b2_init, b3_init, labor)

'''
The steady state values are:
c1 = 0.184
c2 = 0.210
c3 = 0.241
b2 = 0.0193
b3 = 0.0584
w = 0.202
r = 2.433
'''

#Problem 2
beta2 = 0.55
b_args2 = (delta, alpha, beta2, sigma, A)
print('Problem 2')
result2 = SS_OLG(b_args2, b2_init, b3_init, labor)

'''
The new steady state values are:
c1 = 0.196
c2 = 0.229
c3 = 0.267
b2 = 0.028
b3 = 0.077
w = 0.244
r = 1.886
When beta increases, the steady state values of consumption, savings, and
wage all increase whereas the steady state of interest decreases. Since the
agent is more patient, then the patient is willing to save and put off consumption,
thus savings are higher for both periods. In turn, this allows for more production
since capital has increased, which leads to more consumption. In addition, since
capital increases, then interest decreases whereas the wage increases as posited
by the firm's problem.
'''

#Problem 3
b_init = np.array([0.8*result1[0], 1.1*result1[1]])
tpi_args = (delta, alpha, beta, sigma, A, T, TPI_tol, xi)
K_TPI = get_K(b_init, tpi_args, result1, labor)

'''
Transition path of capital is 30 periods:
[ 0.07970223  0.07540149  0.07784571  0.07716849  0.07766605  0.07757797
  0.07768647  0.07768198  0.07770792  0.07771092  0.07771776  0.07771958
  0.07772155  0.0777223   0.07772291  0.07772319  0.07772338  0.07772348
  0.07772354  0.07772358  0.0777236   0.07772361  0.07772362  0.07772362
  0.07772362  0.07772362  0.07772363  0.07772363  0.07772363  0.07772363]
'''
#Problem 4
xvals = np.arange(30)
fig, ax = plt.subplots()
plt.plot(xvals, K_TPI)
minorLocator = MultipleLocator(1)
ax.xaxis.set_minor_locator(minorLocator)
plt.grid(b=True, which='major', color='0.65', linestyle='-')
plt.title('Transition Path for Capital Stock', fontsize=20)
plt.xlabel('Period')
plt.ylabel('Capital Stock')
plt.savefig('timepathiteration.png')
plt.show()
plt.close

'''
As shown by the image "timepathiteration.png", the equilibrium time path of
the aggregate capital stock oscillates around the steady state, and converges
by period 12.
'''
