a = int(input("Enter i:"))
i = a
result = a
while i > 1:
    result = result * (i - 1)
    i -= 1
print("%s!=%s"%(a,result))
