class A():
    """
    __doc__的表现
    """
    name1 = 1
    def a(self):
        pass

    def __init__(self,name):
        self.name = name

    def __del__(self):
        print('delete')

    def __call__(self, *args, **kwargs):
        print('call')

    def show(self):
        print(self.name)

    def __str__(self):
       return self.name

if __name__ == '__main__':
    print(A.__doc__)
    a1 = A('apple')
    print(a1.name1)
    print()
    print(a1.__class__)
    print(A.__module__)
    b1 = A('banana')
    print(b1.name,'*')
    b1.__del__()
    a1()
    print(A.__dict__)
    print(a1.__dict__)
    print(a1)


