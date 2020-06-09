"""
Ввести "exit" для завершения ввода x
"""

def function_2(x):
    """
    Functions calculation
    :param x: value X
    :type x: int
    :return: F(x)
    """
    if x >= -2 and x < 2:
        return x ** 2
    elif x >= 2:
        return x ** 2 + 4 * x + 5
    else:
        return 4


sequence_x = list()
sequence_f = list()
n = 0

while True:
    n += 1
    user_text = input(f'Enter x{n}:')
    if user_text == "exit":
        break
    sequence_x.append(int(user_text))

print(f'Последовательность введенных X: {sequence_x}')

for i in sequence_x:
    sequence_f.append(function_2(i))

print(f'Результат вычисления F(x): {sequence_f}')

max_value = sequence_f[0]

for i in sequence_f:
    if i > max_value:
        max_value = i

print(f'Максимальное значение F(x): {max_value}')
