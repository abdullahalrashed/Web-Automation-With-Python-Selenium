from udemy_practice import Calculator

class childinl(Calculator):
    num2= 200

    def __init__(self):
        Calculator.__init__(self,2 , 10)

    def get_complete_data(self):
        return self.num2 + self.num + self.summation()

obj = childinl()
obj.get_complete_data()
print(obj.get_complete_data())


# 1. Create a function called CalculateAverage that takes three parameters
def CalculateAverage(num1, num2, num3):
    # Calculate the sum of the three numbers
    total = num1 + num2 + num3

    average = total / 3
    return average

input_num1 = 10
input_num2 = 20
input_num3 = 30

result = CalculateAverage(input_num1, input_num2, input_num3)

print(f"The average of {input_num1}, {input_num2}, and {input_num3} is {result}")