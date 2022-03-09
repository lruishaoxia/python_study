<<<<<<< HEAD
def change(num):

    num = 20
    print(num)
    print(id(num))

def change_str(str):
    str = str +'123'
    print(str)
    print(id(str))

def change_tuple(tuple):
    tuple = tuple +(1,2.3)
    print(tuple)
    print(id(tuple))

def change_list(list):
    list[0]=2
    print(list)
    print(id(list))

def change_dic(dic):
    dic[1]=2
    print(dic)
    print(id(dic))

if __name__ == '__main__':
    change(10)
    print(id(10))
    print('*'*50)

    change_str('hello')
    print(id('hello'))
    print('*'*50)

    x = (9,8,7)
    change_tuple((x))
    print(id(x))
    print('*'*50)

    y = [9,8,7]
    change_list(y)
    print(id(y))
    print('*'*50)

    z = {"1":"h",
         "2":"e",
         "3":"l"}
    change_dic(z)
    print(id(z))
=======
def change(num):

    num = 20
    print(num)
    print(id(num))

def change_str(str):
    str = str +'123'
    print(str)
    print(id(str))

def change_tuple(tuple):
    tuple = tuple +(1,2.3)
    print(tuple)
    print(id(tuple))

def change_list(list):
    list[0]=2
    print(list)
    print(id(list))

def change_dic(dic):
    dic[1]=2
    print(dic)
    print(id(dic))

if __name__ == '__main__':
    change(10)
    print(id(10))
    print('*'*50)

    change_str('hello')
    print(id('hello'))
    print('*'*50)

    x = (9,8,7)
    change_tuple((x))
    print(id(x))
    print('*'*50)

    y = [9,8,7]
    change_list(y)
    print(id(y))
    print('*'*50)

    z = {"1":"h",
         "2":"e",
         "3":"l"}
    change_dic(z)
    print(id(z))
>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
    print('*' * 50)