# # 函数的简单入参练习(递归)
# def result1(a):
#     if 0 <= a <= 3:
#         return a
#     return result1(a-1)+result1(a-2)
#
# if __name__ == '__main__':
#     print(result1(5))
#
# def change(a):
#     a[0] = 9909
#     return a
# def change1(b):
#     b['name'] = 'wukong'
#     return b
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#     print(a)
#     print(id(a))
#     print(change(a))
#     print(id(a))
#     print('*' * 50)
#     b = {'name': 'bajie', 'gender': 'man'}
#     print(b)
#     print(id(b))
#     print(change1(b))
#     print(id(b))

# 多个缺省参数的传递练习，练习多个缺省参数
#
# def human(name,gender=True,title=''):
#     gender_text = 'man'
#     if not gender:
#         gender_text = 'woman'
#     print('{}{}是{}'.format(title,name,gender_text))
#
# if __name__ == '__main__':
#     human('xiaoming',title='master')
#     human('xiaoli',gender=False)

# #  可变参数练习，元组，字典的传参拆包练习
# def result1(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# a = (1,3,'r',6)
# b = {'name':'wukong','age':19}
# result1(*a,**b)
#
#
# # 设计一个类，实例化两个对象，然后小明跑步跑完步，会去吃东西
# # 小美不跑步，小美喜欢吃东西
# class Human():
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def run(self):
#         print('%s is running'% self.name)
#     def eat(self):
#         print('%s is eating'%self.name)
#
# xiaoming = Human('xiaoming',18,1.75)
# xiaoming.run()
# xiaoming.eat()
# xiaomei =   Human('xiaomei',17,1.65)
# xiaomei.eat()

# 设计一个类，实例化1个对象，会实现下面两种行为
#
# 需求
# •	一只 黄颜色 的 狗狗 叫 大黄
# •	具有  汪汪叫 行为
# •	具有  摇尾巴 行为

# class Dogs():
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#
#     def bark(self):
#         print('%s汪汪叫' % self.name)
#
#     def shake(self):
#         print('%s摇尾巴' % self.name)
#
#     def __str__(self):
#         return 'wangwang'
#
#     def __del__(self):
#         print('886')
#
#
# dahuang = Dogs('dahuang', 'yellow')
# dahuang.bark()
# dahuang.shake()
# print(dahuang)
# del dahuang

#
# # 练习房子-家具类设计，感受类的设计的先后顺序
# class HouseItem():
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#     def __str__(self):
#         return '{}占地{}'.format(self.name,self.area)
#
#
# class House():
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#         self.freearea =area
#         self.item_list = []
#
#     def __str__(self):
#         return ('该房为{}总面积为{}\n共有家具{}剩余面积为{}'.
#                 format(self.house_type,self.area,self.item_list,self.freearea))
#
#     def add(self,HouseItem):
#
#         if  HouseItem.area > self.freearea:
#             print('{}面积太大家里放不下'.format(HouseItem.name))
#         else:
#
#             self.item_list.append(HouseItem.name)
#             self.freearea-=HouseItem.area
#             print('添加{},房子剩余面积为{}'.format(HouseItem.name,self.freearea))
#
#
# bed = HouseItem('席梦思',4)
# chest = HouseItem('衣柜',2)
# table = HouseItem('餐桌',1.5)
# print(bed)
# print(chest)
# print(table)
# my_house = House('别墅',120)
# print(my_house)
# my_house.add(bed)
# my_house.add(chest)
# print(my_house)

# # 练习私有属性和私有方法
# class Women:
#     def __init__(self,name):
#         self.name = name
#         self.__age = 18
#
#     def __se(self):
#         print('hello')
#
# xiaomei = Women('xiaomei')
# print(xiaomei._Women__age)
# xiaomei._Women__se()
#

# 练习继承、使用super调用父类方法，多重继承
class Animal:
    def eat(self):
        print('is eating')

    def run(self):
        print('is running')

    def sleep(self):
        print('is sleeping')


class Dogs(Animal):
    def bark(self):
        print('is barking')


class Cats(Animal):
    def catch(self):
        print('is catching')


class Shenquan(Dogs):
    def fly(self):
        print('is flying')

    def bark(self):
        # super().bark()
        print('汪汪')


xtq = Shenquan()
xtq.bark()
xtq.fly()
xtq.sleep()
