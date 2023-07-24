# 14. Implement a program to find the common elements between two lists.

element1 = [2,5,6,9]
element2 = [3,5,1,0]

# Common_Element = set(element1).intersection(element2)
# print(Common_Element)

Common_Element = set(element1) & set(element2)
if Common_Element:
    print("Common Element",Common_Element)
else:
    print("Element", Common_Element)