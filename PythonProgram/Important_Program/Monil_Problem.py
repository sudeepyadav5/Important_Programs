"""my_list = [12, 12, 34, 56, 66, 66, 789, 45, 44, 55, 66, 66, 12, 1, 23, 43, 42, 43, 43, 2, 1, 1, 43, 43, 43]

removedublicate = list(set(my_list))
print(removedublicate)

mysort = sorted(removedublicate)
print(mysort)

second_hight_num = mysort[-2]
print(second_hight_num)
"""
my_list = [12, 12, 34, 56, 66, 66, 789, 45, 44, 55, 66, 66, 12, 1, 23, 43, 42, 43, 43, 2, 1, 1, 43, 43, 43]

second_hight_num = sorted(list(set(my_list)))[-2]
print(second_hight_num)
