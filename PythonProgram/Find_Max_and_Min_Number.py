NoOfElement = int(input("Enter N Number of Element You Want: "))
ListOfElement = []
for i in range(NoOfElement):
    element = int(input("Enter Element Value: "))
    ListOfElement.append(element)
print(ListOfElement)
Max_of_Element = max(ListOfElement)
print(f"Maximum Element is {Max_of_Element}")
Min_of_Element = min(ListOfElement)
print(f"Minimum Element is {Min_of_Element}")
