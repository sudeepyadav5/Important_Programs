# from collections import Counter
#
# mylist = [4, 6, 9, 0, 0, 9, 4]
#
# repeted_element = Counter(mylist)
# print(repeted_element)
#
# 11. Write a program to count_of_repeated_element_in_list.
mylist = [4, 6, 9, 0, 0, 9, 4]
Element = {}
for i in mylist:
    if i in Element:
        Element[i] +=1
    else:
        Element[i] = 1
print(Element)









