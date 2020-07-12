
my_list = []
for i in range(100):
    if i < 2:
        my_list.append(1)
    else:
        my_list.append(my_list[i-2]+ my_list[i-1])
        if my_list[i] == 55:
            break
print(my_list)