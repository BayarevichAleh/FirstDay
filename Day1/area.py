import math

print("      /\\")
print("     /__\\")
print("  a /____\\ b")
print("   /______\\")
print("  /________\\")
print("      c      ")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
if c >= (a + b):
    print("Error! You entered incorrect data.")
else:
    p = (a + b + c) / 2
    h = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / c
    print(h)
    s = (c * h) / 2
    print("S=%s" % s)
