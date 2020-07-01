def add(arg1, arg2):
    return arg1 + arg2

def sub(arg1, arg2):
    return arg1 - arg2

def mul(arg1, arg2):
    return arg1 * arg2

def div(arg1, arg2):
    return arg1 / arg2

def calculation(arg1, arg2, operand):
    if operand == '+':
        return add(arg1, arg2)
    elif operand == '-':
        return sub(arg1, arg2)
    elif operand == '*':
        return mul(arg1, arg2)
    elif operand == '/':
        return div(arg1, arg2)
