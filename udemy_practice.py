# # # how to save files in the dictionary
# #
dict = {}

dict[ "firstname" ] = "Abdullah Al"
dict["Lastname"] = "Rashed"
dict["gender"] = "Male"
dict["age"] = 25

print(dict)

########class################

class Calculator:
    num = 100

    def get_data(self):
        print("Executing a method")

obj = Calculator()
obj.get_data()
print(obj.num)
#
# ###################### constructior and types of variable #########################3
#
class Calculator:
    num = 100

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b
        print("I am called automatically when an object is called")

    def get_data(self):
        print("I am now executing a method in class")

    def summation(self):
        return self.first_number + self.second_number + self.num

obj = Calculator(2, 3)
obj.get_data()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.get_data()
print(obj1.summation())
#
#
#
# ############################## BASIC CALCULATOR CALCULATION ################################
#
class BasicCalculator:

    def __init__(self, num1, num2):
        self.first_number = num1
        self.second_number = num2

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number


obj = BasicCalculator(10, 5)
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()

print("Addition: 10+5 = ", obj.addition())
print("Subtraction: 10 - 5 = ", obj.subtraction())
print("Multiplication: 10*5 = ", obj.multiplication())
print("Division: 10/5 = ", obj.division())
#
#
# ###################### READ AND WRITE TXT FILE####################

file = open('test.txt')
#print(file.read(5))      # read(5) represent 5 bytes
#print(file.readline())    # variable.readline() print a line
line = file.readline()
while line != "":
    print(line)             # using while method to read line
    line = file.readline()
file.close()

# --------------

file = open('test.txt')

line = file.readline()
while line != "":
    print(line, end='')
    line = file.readline()

file.close()

# ------

file = open("test.txt")
line_number = 0
line = file.readline()

while line != "":
    line_number = line_number + 1
    line = file.readline()

print("Total number of lines:", line_number)

file.close()


#--------

file = open('test.txt')
for line in file.readlines():  # file.readlines() save the text as a list
    print(line)
file.close()

#---write---

#to read with open('test.txt', 'r') as variable:
# to write with open("test.txt",'w') as variable:

with open("test.txt", 'r') as file:                         #goal: read, write, reverse, list, reverse write
    content = file.readlines() #saved as a list
    reversed(content)
    with open("test.txt", 'w') as file2:
        for line in reversed(content):
            file2.write(line)




#########Exception catch finally keyword use in python#############

ItemsInCart = 0

# 2 items needed to add to the cart with a code [code here]

if ItemsInCart !=2:
    raise Exception("Products cart count not matching")

# -----another way to do this is

ItemsInCart = 0

# 2 items needed to add to the cart with a code [code here]

if ItemsInCart !=2:
    pass
assert(ItemsInCart == 2)   # when the condition inside dosent match assert break the code

# ---------------try and catch

try:
    with open('textt.txt') as reader:  # there is no such file as textt.txt
        reader.read()

except:
    print("i somehow ended up here because of a failure")

# ------------

try:
    with open('textt.txt') as reader:  # there is no such file as textt.txt
        reader.read()

except Exception as e:  # instead of customizable error it shows the python error message
    print(e)

# ------Finally, it will execute whether or not test case execute or not

try:
    with open('textt.txt') as reader:  # there is no such file as textt.txt
        reader.read()

except Exception as e:  # instead of customizable error it shows the python error message
    print(e)

finally:
    print("clean up the record")

# ------------
