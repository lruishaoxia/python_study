# # 实现单例模式
# class Musicplayer:
#     id = None
#
#     @classmethod
#     def __new__(cls, *args, **kwargs):
#         if cls.id is None:
#             cls.id = super().__new__(cls)
#         return cls.id
#
#     def __init__(self,musicname):
#         self.musicname = musicname
#
# if __name__ == '__main__':
#     player1 = Musicplayer('music1')
#     player2 = Musicplayer('music2')
#     print(id(player1))
#     print(id(player2))
#     print(player1.musicname)
#     print(player2.musicname)


# # 通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就不是，非整型抛异常，非对称数抛不抛异常自行选择
#
# def isnum(x):
#     y = str(x)
#     a = list(y)
#     a.reverse()
#     if a == list(y):
#         print('{}是整数也是对称数'.format(x))
#     else:
#         ex = Exception('{}是整数但不是对称数'.format(x))
#         raise ex
#
#
# def isint():
#     try:
#         x = int(input('请输入一个整数'))
#
#     except:
#         print('{}不是一个整数'.format(x))
#     else:
#         try:
#             isnum(x)
#         except Exception as result:
#             print(result)
#
#
# isint()


# 以可读可写打开一个文件，然后写入“人生苦短 我用Python”，关闭文件
import os
# def use_file():
#     file = open('file1.txt',mode='r+',encoding='utf8')
#     file.write('人生苦短 我用Python')
#     file.seek(0)
#     txt = file.read()
#     print(txt)
#     file.close()
#
# use_file()

# # 通过readline依次读取文件每一行并打印
# import os
# def use_file():
#     file = open('file1.txt',mode='r+',encoding='utf8')
#     file.write('人生苦短 我用Python \nhello')
#     file.seek(0)
#     while True:
#         txt = file.readline()
#         print(txt,end='')
#         if not txt:
#             break
#
#
#     file.close()
#
# use_file()

# import os
# a = open('file1.txt',mode='r+',encoding='UTF-8')
# txt = a.read()
# b = open('file2.txt',mode='r+',encoding='UTF-8')
# b.write(txt)
# b.seek(0)
# txt1 = b.read()
# print(txt1)

#
# # 通过seek从文件开头偏移5个字节，然后把文件剩余内容读取
#
# a = open('file2.txt',mode='r+',encoding='UTF-8')
# a.seek(5)
# txt = a.read()
# print(txt)
# a.close()


# a = open('file2.txt',mode='rb+')
# txt = a.read()
# print(txt)


# # 对文件进行改名并删除文件
#
# import os
# os.rename('file1.txt', 'file0.txt')
# os.remove('file0.txt')

# 创建文件夹，删除文件夹（均使用相对路径），改变程序执行路径，获取程序当前路径
import os
os.mkdir('dir1')
print(os.getcwd())

os.chdir('./1')
os.rename('../dir1','dir2')
print(os.getcwd())
os.rmdir('dir2')