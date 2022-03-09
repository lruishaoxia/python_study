for i in range(-3, 0):
    for j in range(0, -i):
        print(' ', end='')
    print('* ' * (5 + i) + ' ' * (-i * 2) + '* ' * (5 + i))
for x in range(0, 10):
    for y in range(0, x):
        print(' ', end='')
    print('* ' * (10 - x))
