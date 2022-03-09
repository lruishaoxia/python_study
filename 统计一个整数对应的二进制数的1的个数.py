x = int(input("请输入一个整数："))
X = list(bin(x))
print(X)
y = 0
# for i in X:
#     if i == '1':
#         y += 1
# print(y)
print(X.count('1'))
