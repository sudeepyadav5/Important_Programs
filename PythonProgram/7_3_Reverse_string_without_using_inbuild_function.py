# Write Program to print reverse string without using inbuilt function

my_String = input("Enter Your String: ")

reverse_String = ''

for i in range(len(my_String)-1,-1,-1):
    reverse_String += my_String[i]
print(reverse_String)

