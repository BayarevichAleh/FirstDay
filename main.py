i = 0
result = 0
while result <= 1000:
    result = result + i;
    i += 1
print(result)
i = int(input("Enter i:"))
result = i
while i > 1:
    result = result * (i - 1)
    i -= 1
print(result)
