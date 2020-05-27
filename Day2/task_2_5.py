string_1 = input("Enter string:")
string_2 = ''
for i in range(0,len(string_1) - 1,+2):
       string_2 += string_1[i]
print(string_2)