# 有102个整数，其中有50个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数。（大家使用8个数即可）

def find_one(a):
    for i in a:
        a.remove(i)
        for j in a:
            if i - j == 0:
                a.remove(i)

    return i

if __name__ == '__main__':
    x =(1, 1, 2, 2, 3, 3, 4, 5)
    b = list(x)
    c = list(x)
    result1 = find_one(b)
    print(result1)
    c.remove(find_one(b))
    result2=find_one(c)
    print(result2)

#
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



