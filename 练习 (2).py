
# def find_one(a):
#     for i in a:
#         a.remove(i)
#         for j in a:
#             if i - j == 0:
#                 break
#     else:print(i)
#
# if __name__ == '__main__':
#     x = [1,2,1,2,3]
#     find_one(x)
#
# #
# # str1 = "6245a"
# # print(str1.splitlines())
#
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)

#
# x = {"apple", "banana", "cherry"}
# # y = {"google", "runoob", "apple"}
# x.update("runoob")
# print(x)

g_num=[1, 2, 34, 3]
b=[1,2]
for i in b:
    g_num.insert(2, i)
print(g_num)