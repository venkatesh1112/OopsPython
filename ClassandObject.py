# Constructor is created automatically once the object is created for the class
# Constructor name should be __init__
# Class Variable - The variable which is created immediate in the class is called Class Variable, CLASS VARIABLES ARE CONSTANT
# Instance Variable - The variable which is inside the constructor is called instance variable. INSTANCE VARIABLES ARE NOT CONTANT
# In Python, variables always calls using self - Example: self.firstname
# new keyword is not required when you create object for the class

class Calculator:
    num = 20

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def sum(self):
        print("sum of given number is: ", self.firstNumber+self.secondNumber)

    def sub(self):
        print("sum of given number is: ", self.firstNumber-self.secondNumber)

    def mul(self):
        print("sum of given number is: ", self.firstNumber*self.secondNumber)


obj_sum = Calculator(3, 5)
obj_sum.sum()

obj_sub = Calculator(3, 5)
obj_sub.sub()

obj_mul = Calculator(3, 5)
obj_mul.mul()


