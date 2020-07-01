
def if_num(data):
    if data == '':
        return ''
    num = 0
    try:
        num = float(data)
    except:
        print("Error! Incorrect data")
    else:
        return num

def if_operand(data):
    if data == '':
        return ''
    if data == '+':
        return '+'
    elif data == '-':
        return '-'
    elif data == '*':
        return '*'
    elif data == '/':
        return '/'
    else:
        print("Error! Incorrect data")

def if_not_zero(data):
    if data != 0:
        return data
    else:
        print("Error! Division by zero is not allowed")




