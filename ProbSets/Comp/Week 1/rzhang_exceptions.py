from random import choice

# Problem 1
def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                            "digits differ by 2 or more: ")
    if int(step_1) > 999 or int(step_1) < 100:
        raise ValueError("Did not enter a 3-digit number")
    if abs(int(step_1[0]) - int(step_1[2])) < 2:
        raise ValueError("First and last digits do not differ by 2 or more")

    step_2 = input("Enter the reverse of the first number, obtained "
                            "by reading it backwards: ")
    if int(step_2[0]) != int(step_1[2]) or int(step_2[1]) != int(step_1[1]) \
        or int(step_2[2]) != int(step_1[0]):
        raise ValueError("Did not enter the reverse of the first number")

    step_3 = input("Enter the positive difference of these numbers: ")
    if int(step_3) != abs(int(step_1) - int(step_2)):
        raise ValueError("Did not enter the positive difference")

    step_4 = input("Enter the reverse of the previous result: ")
    if int(step_4[0]) != int(step_3[2]) or int(step_4[1]) != int(step_3[1]) \
        or int(step_4[2]) != int(step_3[0]):
        raise ValueError("Did not enter the reverse of the previous result")

    print (step_3 + "+" + step_4 + "= 1089 (ta-da!)")

arithmagic()

# Problem 2
def random_walk(max_iters=1e12):
    walk = 0
    direction = [1,-1]
    for i in range(int(max_iters)):
        try:
            walk += choice(direction)
        except KeyboardInterrupt:
            print("Process interrupted at iteration " + str(i))
            return walk
    print("Process completed")
    return walk

print(random_walk())

# Problem 3 and 4
class ContentFilter(object):
    def __init__(self,name):
        try:
            if not isinstance(name,str):
                raise TypeError
        except TypeError:
            print("TypeError: File name not a string")
        else:
            self.name = name
            with open(name,'a') as file:
                file.write('')
            with open(name,'r') as file2:
                self.contents = file2.read()

    def uniform(self,name_to,mode='w',case='upper'):
        if mode!='w' and mode !='a':
            raise ValueError("Invalid mode. Must be 'w' or 'a'")
        if case!='upper' and case !='lower':
            raise ValueError("Invalid case. Must be 'upper' or 'lower'")
        if case == 'upper':
            with open(name_to,mode) as out_file:
                out_file.write(self.contents.upper())
        if case == 'lower':
            with open(name_to,mode) as out_file:
                out_file.write(self.contents.lower())

    def reverse(self,name_to,mode='w',unit='line'):
        if mode!='w' and mode !='a':
            raise ValueError("Invalid mode. Must be 'w' or 'a'")
        if unit!='line' and unit!='word':
            raise ValueError("Invalid reverse style. Must be 'word' or 'line'")
        if unit=='word':
            lines = self.contents.split('\n')
            with open(name_to,mode) as out_file:
                for i in lines:
                    words = i.split()
                    for j in reversed(words):
                        out_file.write(j+' ')
                    out_file.write('\n')
        if unit=='line':
            lines = self.contents.split('\n')
            with open(name_to,mode) as out_file:
                for i in reversed(lines):
                    out_file.write(i+'\n')

    def transpose(self,name_to,mode='w'):
        if mode!='w' and mode !='a':
            raise ValueError("Invalid mode. Must be 'w' or 'a'")
        # assume equal number of words on each line of the input file
        lines = self.contents.split('\n')
        line_num = len(lines)

        words_per_line = len(lines[0].split())
        tot_words = self.contents.split()

        with open(name_to,mode) as out_file:
            for i in range(words_per_line):
                for j in range(line_num):
                    out_file.write(tot_words[j*words_per_line+i]+" ")
                out_file.write('\n')

    def __str__(self):
        char = len(self.contents)
        alph = 0
        num = 0
        white = 0
        for i in range(len(self.contents)):
            if self.contents[i].isalpha():
                alph = alph+1
            elif self.contents[i].isdigit():
                num = num+1
            elif self.contents[i].isspace():
                white = white+1
        source = "Source file:           " + self.name + "\n"
        tot_char = "Total characters:      " + str(char) + "\n"
        alph_char = "Alphabetic characters: " + str(alph) + "\n"
        num_char = "Numerical characters:  " + str(num) + "\n"
        white_char = "Whitespace characters: " + str(white) + "\n"
        lines = "Number of lines:       " + str(len(self.contents.split('\n')))
        return source+tot_char+alph_char+num_char+white_char+lines

file = ContentFilter("hello.txt")
print(file)
file.uniform("hello_up.txt")
file.uniform("hello_low.txt",'w','lower')
file.reverse("hello_line.txt")
file.reverse("hello_word.txt",'w','word')
file.transpose("hello_trans.txt")
file2 = ContentFilter(12)
