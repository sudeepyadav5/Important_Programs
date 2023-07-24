num = input("Enter the Input")
reversed = ''
for i in range(len(num)-1,-1,-1):
    reversed += num[i]
print(reversed)
