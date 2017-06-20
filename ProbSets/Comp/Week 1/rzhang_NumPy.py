import numpy as np

def problem1():
    A = np.array([[3, -1, 4],[1, 5, -9]])
    B = np.array([[2, 6, -5, 3],[5, -8, 9, 7],[9, -3, -2, -3]])
    return np.dot(A, B)

def problem2():
    A = np.array([[3, 1, 4],[1, 5, 9],[-5, 3, 1]])
    return -np.dot(np.dot(A,A),A)+9*np.dot(A,A)-15*A

def problem3():
    A = np.triu(np.ones((7,7)))
    B = np.tril(np.full((7,7),-6))+5
    ABA = np.dot(np.dot(A,B),A)
    return ABA.astype(np.int64)

def problem4(A):
    mask = A < 0
    A[mask] = 0
    return A

def problem5():
    A = np.array([[0, 2, 4],[1, 3, 5]])
    B = np.tril(np.full((3,3),3))
    C = np.eye(3)*-2
    zero1 = np.full_like(B,0)
    zero2 = np.zeros((2,3))
    zero3 = np.zeros((2,2))
    I = np.eye(3)
    row2 = np.hstack((A,zero3,zero2))
    row1 = np.hstack((zero1,A.T,I))
    row3 = np.hstack((B,zero2.T,C))
    return np.vstack((row1,row2,row3))

def problem6(A):
    A.astype(np.float64)
    x = A.sum(axis=1)
    y = x.reshape((x.size,1))
    return A/y

def problem7():
    grid = np.load(r"/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/Computation/Wk1_PyIntro/grid.npy")
    win_h = np.max(grid[:,:-3]*grid[:,1:-2]*grid[:,2:-1]*grid[:,3:])
    win_v = np.max(grid[:-3,:]*grid[1:-2,:]*grid[2:-1,:]*grid[3:,:])
    win_rd = np.max(grid[:-3,:-3]*grid[1:-2,1:-2]*grid[2:-1,2:-1]*grid[3:,3:])
    win_ld = np.max(grid[3:,:-3]*grid[2:-1,1:-2]*grid[1:-2,2:-1]*grid[:-3,3:])
    return np.max([win_h,win_v,win_rd,win_ld])

test = np.array([[1,-5,3],[-3,8,9],[-44,3,2]])
test2 = np.array([[1,5,3],[3,8,9],[44,3,2]])
print (problem1())
print (problem2())
print (problem3())
print (problem4(test))
print (problem5())
print (problem6(test2))
print (problem7())
