class Animal():
    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗汪汪叫')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫喵喵叫')


class FactoryMode():
    def creat(self, name):
        if name == 'dog':
            return Dog
        if name == 'cat':
            return Cat


if __name__ == '__main__':
    f = FactoryMode()
    a = f.creat('cat')()
    a.eat()
    a.voice()
