for i in range(-4, 5):
    if i <= 0:
        for j in range(0, -i):
            print(" ", end='')
        print('* ' * (5 + i))
    elif i > 0:
        for j in range(0, i):
            print(" ", end='')
        print('* ' * (5 - i))

x = int(input("请输入菱形对角线长度(奇数)："))
for i in range(-(x // 2), (x // 2 + 1)):
    if i <= 0:
        for j in range(0, -i):
            print(" ", end='')
        print('* ' * ((x // 2 + 1) + i))
    elif i > 0:
        for j in range(0, i):
            print(" ", end='')
        print('* ' * ((x // 2 + 1) - i))
