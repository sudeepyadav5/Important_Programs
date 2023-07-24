def logData(func):
    def wrapper(*args, **kwargs):
        print("*******************")
        print(f"{func.__name__} output:")
        result = func(*args, **kwargs)
        print(result)
        print("*******************")
        return result
    return wrapper

@logData
def sumOfNumber(a, b):
    c = a + b
    return c

sumOfNumber(2, 5)
