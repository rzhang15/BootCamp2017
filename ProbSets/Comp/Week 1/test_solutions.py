# test_solutions.py
"""Volume 1B: Testing.
Ruby Zhang
OSML Boot Camp
Jun 27, 2017
"""

import solutions as soln
import pytest
import math


# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(2.2,4.3)==6.5, "Addition failed on positive numbers"
    assert soln.addition(-4.2,-7.2)==-11.4, "Addition failed on negative numbers"
    assert soln.addition(-5.5,8)==2.5, "Addition failed on numbers"

def test_smallest_factor():
    assert soln.smallest_factor(1)==1, "Smallest prime factor failed on 1"
    assert soln.smallest_factor(5)==5, "Smallest prime factor failed on prime factor"
    assert soln.smallest_factor(27)==3, "Smallest prime factor failed on composite number"

# Problem 2: Test the operator function from solutions.py
def test_operator():
    with pytest.raises(Exception) as excinfo:
        soln.operator(4, 5, 4)
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Oper should be a string"

    with pytest.raises(Exception) as excinfo:
        soln.operator(4, 5, "**")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Oper should be one character"

    with pytest.raises(Exception) as excinfo:
        soln.operator(4, 0, "/")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="You can't divide by zero!"

    with pytest.raises(Exception) as excinfo:
        soln.operator(4, 5, "&")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Oper can only be: '+', '/', '-', or '*'"

    assert soln.operator(-50.3, 7, "+")==-43.3, "Operator failed on addition"
    assert soln.operator(-6, 4, "/")==-1.5, "Operator failed on division"
    assert soln.operator(-50.3, 7, "-")==-57.3, "Operator failed on subtraction"
    assert soln.operator(5.3, -4.7, "*")==-24.91, "Operator failed on multiplication"

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.conjugate() == soln.ComplexNumber(1,-2)
    assert number_2.conjugate() == soln.ComplexNumber(5,-5)
    assert number_3.conjugate() == soln.ComplexNumber(2,-9)

def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.norm() == math.sqrt(5)
    assert number_2.norm() == math.sqrt(50)
    assert number_3.norm() == math.sqrt(85)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3, -4)
    assert number_3 - number_3 == soln.ComplexNumber(0, 0)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    number_4 = soln.ComplexNumber(0,0)
    assert number_1/number_2 == soln.ComplexNumber(0.3,0.1)
    assert number_1/number_3 == soln.ComplexNumber(4/17,-1/17)
    assert number_3/number_3 == soln.ComplexNumber(1,0)

    with pytest.raises(Exception) as excinfo:
        number_2/number_4
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Cannot divide by zero"

def test_complex_equal(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 != number_2
    assert number_1 != number_3
    assert number_2 != number_3
    assert number_3 == number_3

def test_complex_string(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1) == "1+2i"
    assert str(number_2) == "5+5i"
    assert str(number_3) == "2+9i"

# Problem 4: Write test cases for the Set game.
def test_valid_card():
    with pytest.raises(Exception) as excinfo:
        soln.valid_card("012")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Incorrect number of arguments"

    with pytest.raises(Exception) as excinfo:
        soln.valid_card("1423")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Invalid attributes"

    assert soln.valid_card("0000")
    assert soln.valid_card("1201")

def test_is_set():
    assert soln.is_set(1022,2021,20)
    assert soln.is_set(1122,10,2201)
    assert not soln.is_set(1000,20,1020)

def test_set_number():
    with pytest.raises(Exception) as excinfo:
        soln.set_number("/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/ProbSets/Comp/Week 1/hands/invalid_card.txt")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Invalid attributes"

    with pytest.raises(Exception) as excinfo:
        soln.set_number("/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/ProbSets/Comp/Week 1/hands/too_few_card.txt")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Incorrect number of cards"

    with pytest.raises(Exception) as excinfo:
        soln.set_number("/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/ProbSets/Comp/Week 1/hands/dupli_card.txt")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="Duplicate cards"

    with pytest.raises(Exception) as excinfo:
        soln.set_number("/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/ProbSets/Comp/Week 1/hands/testing.txt")
    assert excinfo.typename=='ValueError'
    assert excinfo.value.args[0]=="File does not exist"

    assert soln.set_number("/Users/rubyzhang/Desktop/UChicago/OSML/BootCamp2017/ProbSets/Comp/Week 1/hands/test.txt") == 6
