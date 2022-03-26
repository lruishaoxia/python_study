class A():
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('A')
        self.func()
        print('A')

@A
def a1():
    print('a1')


# a11 = A(a1)
# a11()
a1()