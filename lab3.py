a = [1, 2, 3]
b = {"x", "y", "z"}
c = (10, 20, 30)
d = {"x1": 10, "x2": 5, "x5": 9}

"""
1. Implement unpack using * and **
2. Implement unpack in function argument * and **
"""


def fun(*x):
    print(x)
    print(type(x))
    sum = 0
    for item in x:
        sum = sum + item
    print(sum)


fun(*a)
