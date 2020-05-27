data = "sasha 4b3, masha 23".replace(',', '').split()
correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sasha_age = ''
masha_age = ''
age = ''
flag = 0
for i in data:
    for k in i:
        if k.isdigit() and int(k) in correct:
            age += k
sasha_age = int(age[0:2])
masha_age = int(age[2:4])
data_2 = [sasha_age,masha_age]
for i in range(0,3,+2):
    print(f"Name: {data[i]} age: {data_2[int(i / 2)]}")