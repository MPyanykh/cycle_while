my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i in range(i, len(my_list)):
    x = my_list[i]
    i += 1
    if x > 0:
        print(x)
    elif x == 0:
        continue
    else:
        break