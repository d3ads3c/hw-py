my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = my_list[:5:1] + my_list[4::-1]
right = my_list[-1:4:-1] + my_list[5::1]
print(left)
print(right)
