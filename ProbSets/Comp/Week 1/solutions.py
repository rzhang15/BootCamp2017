# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math
import os.path

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        #print (str(ComplexNumber(top.real / bottom, top.imag / bottom)))
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here
def valid_card(card):
    valid = False
    if len(card)!=4:
        raise ValueError("Incorrect number of arguments")
    for i in range(0,4):
        if int(card[i]) < 0 or int(card[i])>2:
            raise ValueError("Invalid attributes")
        elif i==3:
            valid = True
    return valid

def is_set(a, b, c):
    is_it = True
    total = sum([a,b,c])
    for i in [1000,100,10,1]:
        if (total//i) % 3 !=0:
            is_it = False
            break
        else:
            total = total%i
    return is_it

def set_number(file):
    if not os.path.isfile(file):
        raise ValueError("File does not exist")
    with open(file) as f:
        cards = f.read().splitlines()
    if len(cards)!=12:
        raise ValueError("Incorrect number of cards")
    for c in cards:
        valid_card(c)
    sets = 0
    for i in range(0,12):
        for j in range (i+1,12):
            for k in range (j+1,12):
                if cards[k]==cards[j] or cards[k]==cards[i]:
                    raise ValueError("Duplicate cards")
                if is_set(int(cards[i]),int(cards[j]),int(cards[k])):
                    sets = sets+1
                k = k+1
            j = j+1
        i = i+1
    return sets
