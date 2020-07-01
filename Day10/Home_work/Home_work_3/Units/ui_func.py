from exceptions import *
from func import *

def interface():
    data = None
    result = None
    operand = None
    index = 0
    while data != '':
        if index == 0:
            data = if_num(input("Enter number: "))
            if operand == '/':
                data = if_not_zero(data)
            if data != None and data != '':
                if result == None:
                    result = data
                elif operand != None:
                    result = calculation(result,data,operand)
                print(f"Result: {result}")
                index = (index + 1) % 2
        else:
            data = if_operand(input("Enter operand: "))
            if data != None and data != '':
                operand = data
                index = (index + 1) % 2
    print("Сброс")
