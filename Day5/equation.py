from math import tan

quantity = int(input("Enter quantity X:"))
x = {}
y = 0
for i in range(quantity):
    x[f'Z{i + 1}'] = int(input(f'Enter Z{i + 1}:'))
    x[f'B{i + 1}'] = int(input(f'Enter B{i + 1}:'))
    x[f'A{i + 1}'] = int(input(f'Enter A{i + 1}:'))
    x[f'C{i + 1}'] = int(input(f'Enter C{i + 1}:'))
    x[f'X{i + 1}'] = x[f'Z{i + 1}'] ** 3 - x[f'B{i + 1}'] + (x[f'A{i + 1}'] ** 2 / tan(x[f'C{i + 1}'] ** 2))
    y += x[f'X{i + 1}']

print(y)
