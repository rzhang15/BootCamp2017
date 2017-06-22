from math import sqrt

# Problems 1 and 3
class Backpack(object):
    '''Additional Practice
    try:
        if self.ID >= 1:
            ID = self.ID + 1
            print(ID)
    except:
        ID = 1
        print(ID)
    '''
    #Problem 1
    def __init__(self,name,color,max_size=5):
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
        # self.ID = ID

    def put(self,item):
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print("No Room!")

    def take(self,item):
        self.contents.remove(item)

    def dump(self):
        self.contents = []

    #Problem 3
    def __eq__(self,other):
        if self.name==other.name and self.color==other.color \
            and len(self.contents)==len(other.contents):
            return True
        else:
            return False

    def __ne__(self,other):
        return not self==other

    def __str__(self):
        owner = "Owner: \t  "+ self.name + "\n"
        color = "Color: \t  "+ self.color + "\n"
        size = "Size: \t  {}".format(len(self.contents)) + "\n"
        max_size = "Max Size: {}".format(self.max_size) + "\n"
        contents = "Contents: [" + ', '.join(self.contents) + "]"
        return owner + color + size + max_size + contents

def test_backpack():
    testpack = Backpack("Barry","black")
    if testpack.max_size != 5:
        print("Wrong default max_size!")
    print(testpack.name, testpack.color, testpack.max_size, testpack.contents)
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)
    print(testpack)
    print(testpack.contents)
    testpack.put("laptop")
    testpack.put("yogurt")
    testpack.take("paper")
    print(testpack.contents)
    testpack.dump()
    print(testpack.contents)
    testpack2 = Backpack("Barry","black")
    print(testpack==testpack2)
    testpack2.put("beans")
    print(testpack==testpack2)
    # print(testpack.ID, testpack2.ID)
test_backpack()

# Problem 2
class Jetpack(Backpack):
    def __init__(self,name,color,max_size=2,fuel=10):
        Backpack.__init__(self,name,color,max_size)
        self.fuel = fuel

    def fly(self,fuel):
        if fuel <= self.fuel:
            self.fuel = self.fuel - fuel
        else:
            print("Not enough fuel!")

    def dump(self):
        self.contents = []
        self.fuel = 0

def test_jetpack():
    testpack = Jetpack("Barry","black")
    if testpack.max_size != 2:
        print("Wrong default max_size!")
    print(testpack.name, testpack.color, testpack.max_size, testpack.fuel, testpack.contents)
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)
    print(testpack)
    print(testpack.contents)
    testpack.put("laptop")
    testpack.put("yogurt")
    testpack.take("pen")
    print(testpack.contents)
    testpack.fly(11)
    testpack.fly(6)
    print(testpack.fuel)
    testpack.dump()
    print(testpack.contents, testpack.fuel)
    testpack2 = Backpack("Barry","black")
    print(testpack==testpack2)
    testpack2.put("beans")
    print(testpack==testpack2)
    # print(testpack.ID, testpack2.ID)
test_jetpack()

# Problem 4
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __lt__(self,other):
        return abs(self) < abs(other)

    def __gt__(self,other):
        return abs(self) > abs(other)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __ne__(self, other):
        return not self==other

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
        return ComplexNumber(top.real / bottom, top.imag / bottom)

def test_complex_num():
    number_1 = ComplexNumber(1, 2)
    number_2 = ComplexNumber(5, 5)
    if number_1.conjugate() != ComplexNumber(1,-2):
        print('Conjugate error')
    if abs(number_1) != sqrt(5):
        print("Abs error")
    print(number_1 < number_2)
    print(number_1 > number_2)
    print(number_1 == number_1)
    print(number_1 != number_2)
    if number_1 + number_2 != ComplexNumber(6, 7):
        print("Add error")
    if number_1 - number_2 != ComplexNumber(-4, -3):
        print("Sub error")
    if number_1 * number_2 != ComplexNumber(-5, 15):
        print("Mul error")
    if number_1 / number_2 != ComplexNumber(0.3, 0.1):
        print("Div error")
test_complex_num()
