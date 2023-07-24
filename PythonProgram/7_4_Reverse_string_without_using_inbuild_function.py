myinput = input("Enter String")

mylist = list(myinput)

mylength = len(mylist)

for i in range(mylength//2):
    mylist[i], mylist[mylength -i -1] = mylist[mylength -i -1], mylist[i]

reversed = ''.join(mylist)
print(reversed)
