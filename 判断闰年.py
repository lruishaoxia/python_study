year = int(input('请输入年份：'))
print('闰年' if year % 400 == 0 or year % 4 == 0 and year % 4 != 0 else '平年')


