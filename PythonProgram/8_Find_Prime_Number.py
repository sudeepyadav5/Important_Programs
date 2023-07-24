# 8. Implement a program to check whether a number is prime or not.

number = int(input("Enter Number: "))
if number <= 1:
    print("Number is not a Prime")
else:
    is_prime = True
    for Div in range(2,number):
        if number%Div==0:
            is_prime = False
    if is_prime:
        print("Prime NUmber")
    else:
        print("Compite Number")
