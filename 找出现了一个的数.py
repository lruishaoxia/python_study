# 有101个整数，其中有50个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。（大家使用7个数即可）
g_num = [2, 2, 3, 3, 4, 4, 5]

for i in g_num:
    g_num.remove(i)
    for j in g_num:
       if i-j == 0:
           g_num.remove(i)
print(i)