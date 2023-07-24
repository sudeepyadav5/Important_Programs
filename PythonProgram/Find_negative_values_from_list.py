MyList = [9,4,-2,4,-7,8]
NegitiveElement = []
PositiveElement = []
for i in MyList:
    if i >1:
        PositiveElement.append(i)
    else:
        NegitiveElement.append(i)

print("My Positive Element", PositiveElement)
print("My Negative Element", NegitiveElement)