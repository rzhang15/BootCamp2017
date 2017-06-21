import calculator as calc
import box
import random
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
        name = input("Player name: ")
    game = True
    num_left = list(range(1,10))
    dice = list(range(1,7))
    while game:
        print ("Numbers left: ", num_left)
        if sum(num_left) <= 6:
            roll = random.choice(dice)
        else:
            roll = random.choice(dice) + random.choice(dice)
        print ("Roll: ", roll)
        if roll==1:
            if num_left[0]!=1:
                game = False
        else:
            game = box.isvalid(roll,num_left)
        if game:
            remove_text = input("Numbers to eliminate: ")
            remove = box.parse_input(remove_text, num_left)
            while remove==[] or sum(remove)!=roll:
                print("Invalid input")
                remove_text = input("Numbers to eliminate: ")
                remove = box.parse_input(remove_text,num_left)
            for x in remove:
                num_left.remove(x)
            if num_left==[]:
                break
        else:
            print("Game Over!")
            break

    score = sum(num_left)
    print ("Score for player TA: ",score," points")
    if score==0:
        print("Congratulations!! You shut the box!")

test = [1, 4, 2, -3, 5, 8]
print(problem1(test))
problem2()
print("3-4-",problem3(3, 4), "5-12-", problem3(5,12))
problem4()
