class Mylist():
    def __init__(self):
        self.list=[]

    def add(self):
        for i in range(3):
            self.list.append(i)
        print(self.list)

if __name__ == '__main__':
    mylist = Mylist()
    mylist.add()
    for i in mylist.list:
        print(i)

