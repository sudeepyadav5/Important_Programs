# 1. Write a program to find the factorial of a given number.

number = int(input("Enter Number: "))
Factorial = 1
if number<0:
    print("Factorial is Undefined for Negative Numbers.")
elif number == 0:
    print(f"Factorial of Zero is {Factorial}.")
else:
    for i in range(1, number+1):
        Factorial *=i
    print(f"{number}! of the Factorial is {Factorial}.")

# def fac(x):
#     if x > 0:
#         return x * fac(x - 1)
#     else:
#         return 1
#
#
# result = fac(5)
# print(result)