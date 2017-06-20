import calculator as calc
import box
import random as rand
import sys

def problem1(A):
    return [min(A),max(A),float(sum(A))/float(len(A))]

def problem2():
    num1 = 2
    num2 = num1
    num2 += 1
    if num1==num2:
        print ("Numbers are mutable")
    else:
        print ("Numbers are immutable")
    word1 = "hello"
    word2 = word1
    word2 += 'a'
    if word1==word2:
        print("Strings are mutable")
    else:
        print("Strings are immutable")
    list1 = [1,2,3]
    list2 = list1
    list2.append(1)
    if list1==list2:
        print("Lists are mutable")
    else:
        print("Lists are immutable")
    tuple1=(1,2,3)
    tuple2=tuple1
    tuple2 += (1,)
    if tuple1==tuple2:
        print("Tuples are mutable")
    else:
        print("Tuples are immutable")
    dict1 = {1:"b",2:"c"}
    dict2 = dict1
    dict2[1]="a"
    if dict1==dict2:
        print("Dictionaries are mutable")
    else:
        print("Dictionaries are immutable")

def problem3(A,B):
    return calc.sqrt(calc.add(calc.times(A,A),calc.times(B,B)))

def problem4():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = raw_input("Please enter your name: ")
    game = True
    num_left = range(1,10)
    dice = range(1,7)
    while game:
        print ("Numbers left: ", num_left)
        roll = random.choice(dice)
        print ("Roll: ", roll)
        remove = sys.argv

problem2()
problem4()
