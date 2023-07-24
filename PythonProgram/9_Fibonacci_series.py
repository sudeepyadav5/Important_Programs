# 9. Write a program to calculate the Fibonacci sequence up to a given number of terms.

num = int(input("Enter N Number for Fibonacci Series: "))

if num <=0:
    print("Number is Invalid, Number Should be Greater Then 0")
else:
    Fibonacci_series = [0,1]

    if Fibonacci_series == 1:
        print(Fibonacci_series[:1])
    elif Fibonacci_series == 2:
        print(Fibonacci_series)
    else:
        while len(Fibonacci_series) < num:
            Next_series = Fibonacci_series[-1] + Fibonacci_series[-2]
            Fibonacci_series.append(Next_series)
        print(Fibonacci_series)




