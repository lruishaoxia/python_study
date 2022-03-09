# #求两个有序数字列表的公共元素
# x = [1,2,3,4,5,6]
# y = [5,6,7,8,9,10]
#
#
# a = set(x)
# b = set(y)
# z = a.intersection(b)
# print(z)
# print('*'*50)
# for i in x:
#     for j in y:
#         if i == j:
#             print(i)
#
# # 给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
# a = [1,2,3,4,6,8,2,4,8,9,2,2,2,2,2,2,2,2]
# n = len(a)
# print(n)
# for i in a:
#     m =a.count(i)
#     # print('%d,%d'%(i,m))
#     if m > n/2:
#         break
# print(i)

# # 将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
# a = (1,2,3)
# b = {4,5,6}
# c = list(a)+list(b)
# print(c)

# # 在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0。
# a =[1,2,3,4,5,6]
# a.insert(0,7)
# a.append(0)
# print(a)

# # 反转列表 [0,1,2,3,4,5,6,7] 。给出5的索引
# a =  [0,1,2,3,4,5,6,7]
# a.reverse()
# print(a)
# print(a.index(5))

# # 分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
# a = [True,False,0,1,2]
# for i in a:
#
#
#     x = a.count(i)
#     print(i,x)
# print('计数时Ture 和 1 一样，False 和 0 一样')
#
# # 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
# a = [True,1,0,'x',None,'x',False,2,True]
# for i in a :
#     if i == 'x':
#         a.remove(i)
# print(a)

# # 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素
# a=[True,1,0,'x',None,'x',False,2,True]
# a.pop(4)
# print(a)

# # 删除列表中索引号为奇数（或偶数）的元素。
# a=[1,2,3,'a',2,'d']
# b = a[::2]
# c = a[1::2]
# print(b)
# print(c)

# # 清空列表中的所有元素
# a = [1,2,34,56,2]
# a.clear()
# print(a)

# # 对列表 [3,0,8,5,7] 分别做升序和降序排列
# a = [3, 0, 8, 5, 7]
# a.sort()
# print(a)
# b = [3, 0, 8, 5, 7]
# b.sort(reverse=True)
# print(b)

# # 将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
# a = [3,0,8,5,7]
# for i in a :
#     if i > 5:
#         n = a.index(i)
#         a[n]=1
#     elif i <5:
#         m = a.index(i)
#         a[m]=0
# print(a)

# # 遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
# a = ['x', 'y', 'z']
# for i in a :
#     print(i,a.index(i))

# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# c = []
# for i in a:
#     if i %2 == 0 :
#         b.append(i)
#     else:
#         c.append(i)
# print(b)
# print(c)

# # 分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。
# a =  [[6, 5], [3, 7], [2, 8]]
# b = [[6, 5], [3, 7], [2, 8]]
# a.sort()
# print(a)
# c=sorted(b,key=(lambda x:x[1] ))
# print(c)

# # 从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素
# a = [1,4,7,2,5,8]
# b = ['x','y','z']
# b.reverse()
# for i in b :
#         a.insert(3,i)
# print(a)
#
#
# # 快速生成由 [5,50) 区间内的整数组成的列表。
# a = list(range(5,50))
# print(a)
#

# # 将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
# a = ['x','y','z']
# b = [1,2,3]
# c = []
# for i in range(0,3):
#     c.append((a[i],b[i]))
# print(c)

# # 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# b=[]
# for i in a:
#     b.append(i)
# print(b)

# # 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# b=[]
# for i in a.values():
#     b.append(i)
# print(b)

# # 以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# b=[]
# for i in a.items():
#     b.append(i)
# print(b)

# # 向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# a.update({'David': 19})
# a['Cecil']=17
# print(a)

# # 删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# a.pop('Beth')
# print(a)
# a.clear()
# print(a)
#
#
# #  David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# print('David' in a)
# print('Alice' in a)

# # 遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
# a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# for i in a.items():
#     print(i)
#
# # 以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典。
# a = ['A','B','C','D','E','F','G','H']
# b={}
# for i in a:
#     b.update({i:0})
# print(b)

# # 将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
# a =[['a',1],['b',2]]
# b = (('x',3),('y',4))
# x = dict(a)
# y = dict(b)
# print(x)
# print(y)

# # 将元组 (1,2) 和 (3,4) 合并成一个元组。
# a = (1,2)
# b = (3,4)
# c = a + b
# print(c)
#
# # 将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
# a = (1,2,3)
# x = a[0]
# y = a[1]
# z = a[2]
# print(x,y,z)

# # 返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号
# def return1():
#     a = ('Alice','Beth','Cecil')
#     x = a.index('Cecil')
#     return x
# if __name__ == '__main__':
#     print(return1())

# # 返回元组 (2,5,3,2,4) 中元素 2 的个数。
# def ret_num():
#     a = (2,5,3,2,4)
#     x = a.count(2)
#     return x
#
# if __name__ == '__main__':
#     print(ret_num())

#
# # 判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中
# print('Cecil'in ('Alice','Beth','Cecil'))
#

# def ret1():
#     a = (2,5,3,7)
#     b = list(a)
#     b.insert(2,9)
#     c = tuple(b)
#     return c
# if __name__ == '__main__':
#     print(ret1())
#
# #
# # 创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
# a = set({})
# print(type(a))
# a.update({'x','y','z'})
# print(a)

# # 删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增j加元素 ‘w’，然后清空整个集合
# a = {'x','y','z'}
# a.remove('z')
# print(a)
# a.add('w')
# print(a)
# a.clear()
# print(a)

# # 返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
# a = {'A','D','B'}
# b = {'D','E','C'}
# c = a.difference(b)
# print(c)
# d = a.union(b)
# print(d)
# e =a.intersection(b)
# print(e)
# f =a.symmetric_difference(b)
# print(a.isdisjoint(b))
# print({'A','C'}.issubset({'D','C','E','A'}))

# # 去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
# a =[1,2,5,2,3,4,5,'x',4,'x']
# b =  set(a)
# print(list(b))

# # 返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
# a = 'abCdEfg'
# print(a.upper())
# print(a.lower())
# print(a.swapcase())

# # 判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
# a = 'abCdEfg'
# print(a.istitle())
# print(a.islower())
# print(a.isupper())

# # 返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
# # 判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
# # 返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
# # 返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
# # 将字符串 ‘this is python’ 切片成3个单词。
# a = 'this is python'
# def change():
#     return a.capitalize(), a.title()
# def num_count():
#     return a.count('is')
# def appear():
#     return a.find('is'), a.rfind('is')
# if __name__ == '__main__':
#     b, c = a.capitalize(), a.title()
#     print(b)
#     print(c)
#     print(a.startswith('this'))
#     print(a.endswith('python'))
#     print(num_count())
#     e,f = appear()
#     print(e)
#     print(f)
#     print(a.split())
#
# # 返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
# a = 'blog.csdn.net/xufive/article/details/102946961'
# print(a.split('/'))

# # 将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
# a = '2.72, 5, 7, 3.14'
# b = a.split(',')
#
# for i in b:
#     try:
#         c = int(i)
#         print(c)
#     except ValueError:
#         d = float(i)
#         print(d)
# #
# # 判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母
# a = 'adS12K56'
# print(a.isalnum())
# print(a.isdecimal())
# print(a.isalpha())

# # 将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’
# a = 'there is python'
# b = list(a.split())
# n = b.index('is')
# b[n]= 'are'
# c = str(b)
# print(c)
# print(type(c))

# # 清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
# a = '\t python \n'
# print(a)
# b = a.lstrip()
# print(b)
# c = a.rstrip()
# print(c)
# d = a.strip()
# print(d)

# # 将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
# a = 'ok'
# b = 'hello'
# c = 'thank you'
# print(a.ljust(0))
# print(b.ljust(0))
# print(c.ljust(0))
#
# print(a.rjust(9))
# print(b.rjust(9))
# print(c.rjust(9))
#
# print(a.center(10))
# print(b.center(10))
# print(c.center(10))


# # 将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果。
# a = 'Hello, 我是David'
# b = 'OK, 好'
# c = '很高兴认识你'
# print(a.ljust(0))
# print(b.ljust(0))
# print(c.ljust(0))
#
# print(a.rjust(12))
# print(b.rjust(15))
# print(c.rjust(12))
#
# print(a.center(11))
# print(b.center(13))
# print(c.center(10))

# # 将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。
# a = '15'
# b = '127'
# c = '65535'
# print(a.rjust(5))
# print(b.rjust(5))
# print(c.rjust(5))

# # 将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串
# x = ['a','b','c']
#
# n = "|"
# z = n.join(x)
# print(z)
#
# # 将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
# a = 'abc'
# print(','.join(a))
#
# # 从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
# a = input('请输入：')
#
# b = 'Mobile:'+a[0:3]+' '+a[3:7]+' '+a[7:]
# print(b,type(b))
#

# # 从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。
# a = input('输入年份')
# b = input('输入月份')
# c = input('输入日期')
# d = input('输入几时')
# e = input('输入几分')
# f = input('输入几秒')
# x = a+'-'+b+'-'+c+' '+d+':'+e+':'+f
# print(x)
#
# # 给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’。
# a =3.1415926
# b = 2.7182818
# print('pi = {:.4f},e = {:.4f}'.format(a,b))
#
# # 将 0.00774592 和 356800000 格式化输出为科学计数法字符串。
# a= 0.00774592
# b = 356800000
# print('{:.2e},{:.2e}'.format(a,b))

# # 将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。
# a = [0,1,2,3.14,'x',None,'',list(),{5}]
# b = []
# for i in a :
#     b.append(bool(i))
# print(b)

# # 返回字符 ‘a’ 和 ‘A’ 的ASCII编码值。
# def asc(x):
#     return ord(x)
# if __name__ == '__main__':
#     print(asc('a'))
#     print(asc('A'))
#


# # 返回ASCII编码值为 57 和 122 的字符
# def asc_r(x):
#     return chr(x)
# if __name__ == '__main__':
#     print(asc_r(57))
#     print(asc_r(122))

# 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。
g_num = [3, 'a', 5.2, 4, {}, 9, []]
# for i in range(len(a)):
#     if isinstance(a[i],int) or isinstance(a[i],float):
#         if a[i]>3:
#             a[i] =1
#         else:
#             a[i]=0
# print(a)

# for i in a :
#     if type(i)==int or type(i)==float:
#         if i >3:
#             a[a.index(i)] = 1
#         else:
#             a[a.index(i)] = 0
# print(a)
#

#
# # 将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
# a =  [[1], ['a','b'], [2.3, 4.5, 6.7]]
# b = [x for i in a for x in i]
# print(b)

# # 将等长的键列表和值列表转为字典。
# a = ['name','gender','weight']
# b = ['laowang','man',60]
# c = dict(zip(a,b))
# print(c)

# 数字列表求和。
g_num = [1, 23, 4, 534, 6, 345, 7, 234, 1]
result = 0
for i in g_num:
    result += i
print(result)
