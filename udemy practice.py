# # how to save files in the dictionary
#
# dict = {}
#
# dict[ "firstname" ] = "Abdullah Al"
# dict["Lastname"] = "Rashed"
# dict["gender"] = "Male"
# dict["age"] = 25
#
# print(dict)

#########class################

# class Calculator:
#     num = 100
#
#     def get_data(self):
#         print("Executing a method")
#
# obj = Calculator()
# obj.get_data()
# print(obj.num)

###################### constructior and types of variable #########################3

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




























