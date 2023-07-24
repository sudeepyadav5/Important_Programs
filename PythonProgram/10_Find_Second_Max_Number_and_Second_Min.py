"""NoOfElement = int(input("Enter N Number of Element You Want: "))
ListOfElement = []
for i in range(NoOfElement):
    element = int(input("Enter Element Value: "))
    ListOfElement.append(element)
print(ListOfElement)
SortingElement = sorted(ListOfElement)
Second_Max_Number = SortingElement[-2]
print("My Second Max Number is ", Second_Max_Number)
Second_Min_Number = SortingElement[2]
print("My Second Min Number is ", Second_Min_Number)"""

# 10. Implement a program to find the second-largest element in a list of integers.
my_list = [8,4,6,9,8,2]
print(sorted(list(set(my_list)))[-2])