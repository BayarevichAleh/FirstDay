list_1 = [5, 9, 8, 1, 3, 2, 2]
a = 0
end_list = len(list_1) - 1
for i in range(end_list):
    for k in range(end_list):
        if list_1[k] > list_1[k + 1]:
            a = list_1[k + 1]
            list_1[k + 1] = list_1[k]
            list_1[k] = a
print(list_1)
