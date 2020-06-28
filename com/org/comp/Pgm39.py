p = 100


def x1():
    print("------x1()------")
    p = 150
    print("p=", p)


def x2():
    print("------x2()------")
    global p
    p = 180
    print("p=", p)


def x3():
    print("------x3()------")
    print("p=", p)


print("-----------------")
print("p=", p)
x1()
x2()
x3()