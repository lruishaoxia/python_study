def f2(func):
    print('begin')

    def f1():
        print('权限验证')
        func()

    return f1


@f2
def f1():
    print('hello')


def a2(func):
    print('a2d')

    def a3():
        print('a2')
        func()

    return a3


def a4(func):
    print('a4d')

    def a5():
        print('a4')
        func()

    return a5


@a2
@a4
def a1():
    print('a1')


import time


def b2(func):
    def b3():
        starttime = time.time()
        func()
        endtime = time.time()
        use_time = endtime - starttime
        print(use_time)

    return b3


@b2
def b1():
    print('sum = 1+...+100001')
    sum = 0
    for i in range(1, 100001):
        sum = sum + i
    print(sum)


def c2(func):
    print('c2')

    def c3(*args, **kwargs):
        print('c2')
        func(*args, **kwargs)
        print('c2')

    return c3


@c2
def c1(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


def d2(func):
    print('d2')

    def d3(x, y):
        print('d2')
        func(x, y)

    return d3


@d2
def d1(a, b):
    print(a + b)


# 装饰带返回值的函数
def e2(func):
    print('e2')

    def e3():
        print('e2')
        return func()

    return e3


@e2
def e1():
    return 'e1'

from functools import wraps
# 装饰器带参数,@wraps返回被装饰的函数的注释
def g2(levernum):
    def g3(func):
        @wraps(func)
        def g4(*args, **kwargs):
            """
            注释g2
            :param args:
            :param kwargs:
            :return:
            """
            nonlocal levernum
            if levernum == 1:
                print('权限验证1')
            if levernum == 2:
                print('权限验证2')
            return func()

        return g4

    return g3


@g2(1)
def g1():


    """
    注释g1
    """
print('g1')
pass

if __name__ == '__main__':
    # f1()
    # a1()
    # b1()
    # c1(1,2,3,name='l')
    # d1(1,2)
    # val = e1()
    # print(e1())
    g1()
    print(g1.__doc__)
