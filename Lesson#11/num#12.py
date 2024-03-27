import math

class1 = int(input('children in first class'))
class2 = int(input('children in second class'))
class3 = int(input('children in third class'))

tables = math.ceil((class1 + class2 + class3) // 2) 

print(f"you need {tables} tables ")