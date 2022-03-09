# class Cat():
#     def eat(self):
#         print('%s爱吃鱼'self.name)
#
#     def drink(self):
# #         print('%s喝水'%self.name)
# #     tom = Cat()
#
#
# def demo(num, num_list):
#     print("函数内部")
# # 赋值语句
#     num = 200
#     num_list = [1, 2, 3]
#     print(num)
#     print(num_list)
#     print("函数代码完成")
# gl_num = 99
# gl_list = [4, 5, 6]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)

# def mutable(num_list):
#     # num_list = [1, 2, 3]
#     num_list.extend([1, 2, 3])
#     print(num_list)
# gl_list = [6, 7, 8]
# mutable(gl_list)
# print(gl_list)


# def demo(num, num_list):
#     print("函数内部代码")
# # num = num + num
#     num += num
# # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
# # 函数执行结束后，外部数据同样会发生变化
#     num_list += num_list
#     print(num)
#     print(num_list)
#     print("函数代码完成")
# gl_num = 9
# gl_list = [1, 2, 3]
# print(gl_list)
# print(id(gl_list))
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)
# print(id(gl_list))
#
# def add(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(add(1, 2.3))

#
# def sum_numbers(*args):
#     num = 0
# # 遍历 args 元组顺序求和
#     for n in args:
#         num += n
#     return num

# print(sum_numbers(1, 2, 3))
#
# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# # 需要将一个元组变量/字典变量传递给函数对应的参数
# gl_nums = (1, 2, 3)
# gl_xiaoming = {"name": "小明", "age": 18}
# # 会把 num_tuple 和 xiaoming 作为元组传递个 args
# # demo(gl_nums, gl_xiaoming)
# demo(*gl_nums, **gl_xiaoming)

