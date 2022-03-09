<<<<<<< HEAD
x = int(input('请输入对角线长度（奇数）:'))
for i in range(-(x // 2), (x // 2 + 1)):
    if i == -(x // 2):
        print(' '*(x//2)+'*')
    if -(x // 2)<i <= 0:
        for j in range(0, -i):
            print(' ',end='')
        print('*'+' '*((x//2+i)*2-1)+'*')
    if 0<i<(x//2):
        for j in range(0, i):
            print(' ',end='')
        print('*'+' '*((x//2-i)*2-1)+'*')
    if i == (x // 2):
        print(' '*(x//2)+'*')

=======
x = int(input('请输入对角线长度（奇数）:'))
for i in range(-(x // 2), (x // 2 + 1)):
    if i == -(x // 2):
        print(' '*(x//2)+'*')
    if -(x // 2)<i <= 0:
        for j in range(0, -i):
            print(' ',end='')
        print('*'+' '*((x//2+i)*2-1)+'*')
    if 0<i<(x//2):
        for j in range(0, i):
            print(' ',end='')
        print('*'+' '*((x//2-i)*2-1)+'*')
    if i == (x // 2):
        print(' '*(x//2)+'*')

>>>>>>> e2c43e045d170dddd8b48902e123096581e081ef
