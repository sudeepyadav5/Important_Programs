myinput = int(input("Enter Year: "))
if myinput == 0:
    print("This Input is Invalid, Please Enter Valid Year ")
elif myinput % 2 == 0 and myinput % 100 != 0 or myinput % 400 == 0:
    print(f"{myinput} is Leap Year")
else:
    print(f"{myinput} is Not a Leap Year")
