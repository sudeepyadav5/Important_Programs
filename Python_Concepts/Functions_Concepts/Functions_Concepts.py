# Non - Parameter Function
def methodOne():
    print("I calling Method One, My Name Is Sudeep Yadav ")


methodOne()


# Parameter Function
def methodTwo(name, age):
    print("My Name is ", name)
    print("My Age is", age)


methodTwo("sudeep", "30")


# Return Type Function

def methodThree(a, b):
    c = a + b
    return c


# print(methodThree(2,5))
d = methodThree(2, 5)
print(d)


# Default Value in the function
def sumoftwoNumber(a, b=9):
    k = a + b
    return k


sum = sumoftwoNumber(9)
print(sum)


# Pass the List value to the function
# def myList(list):
#     for i in list:
#         print(i)
# mydata = [1, 4, 3, 7, 5, 9, 2]
# myList(mydata)

# Arrange in Order of list
def myFun(mylist):
    Orderlist = sorted(list(set(mylist)))[-2]
    print(f"My OrderList of 2nd Largest {Orderlist}")


mydata = [1, 4, 3, 1, 7, 7, 5, 3, 2, 9, 10, 2]
myFun(mydata)


# key and value as Argument

# def empData(name, age, number):
#     print("Name is ", name)
#     print("Age is", age)
#     print("Number is", number)
#
# empData(age=100, number="9090909090", name="sudeep")

# Arbitrary Keyword Argument, **kwargs
def empData(**kwargs):
    print(kwargs)


empData(age="30", name="sudeep")


def stdData(**kwargs):
    print(kwargs)


stdData(std='Computer Science', teachername='')

def methodFive():
    pass


