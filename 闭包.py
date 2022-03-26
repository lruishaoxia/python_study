def f1(k,b):
    def f2(x):
        print(k*x+b)
    return f2

F1 = f1(2,3)
F1(1)


num = 100
def f3():
    num = 1
    print(num)
    def f4():
        nonlocal num
        num =2
        print(num)
    return f4

F2 = f3()
F2()

