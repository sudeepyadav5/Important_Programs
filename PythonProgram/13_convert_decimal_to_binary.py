# 13. Write a program to convert a decimal number to binary representation.

Decimal_Number = int(input("Enter Decimal Number: "))

Binary_Number = bin(Decimal_Number)
print(f"Decimal Number is {Decimal_Number} and  Binary Number {Binary_Number[2:]}")
