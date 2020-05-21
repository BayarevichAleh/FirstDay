import math

print("    angle")
print("      /\\")
print("     /__\\")
print("  a /____\\ b")
print("   /______\\")
print("  /________\\")
print("      c      ")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
angle = int(input("Enter angle:"))
c = math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(angle))))
h = math.sqrt((a ** 2) - ((c / 2) ** 2))
s = c / 2 * h
print("S=%s" % s)
