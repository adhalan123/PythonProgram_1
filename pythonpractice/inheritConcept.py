class parent1:
    test =0

    def __init__(self,first,second):
        self.firstNumber=first
        self.secondNumber=second
        print(first, second)

    def summation(self, a, b):
        return a+b

obj=parent1(45,67)
print("sum of this number=",obj.summation(10, 56))