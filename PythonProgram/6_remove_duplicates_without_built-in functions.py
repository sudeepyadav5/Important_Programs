# 6. Implement a program to remove duplicates from a list without using any built-in functions.

myList = [7,5,5,9,3,5,7,0,9,1]
unique = []
for item in myList:
    if item not in unique:
        unique.append(item)
print(f"Original List {myList}")
print("After Removed Duplicate Element is ", unique)