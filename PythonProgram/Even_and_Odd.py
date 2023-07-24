element = int(input("Enter N of the Element for Odd & Even: "))
myEven = []
Evensum = 0
myOdd = []
Oddsum = 0
for i in range(1, element):
    if i % 2 == 0:
        myEven.append(i)
        Evensum +=i
    else:
        myOdd.append(i)
        Oddsum +=i

print(f"Even Number is {myEven} and Sum of Even Number is {Evensum}")

print(f"Odd Number is {myOdd} and Sum of Odd Number is {Oddsum}")