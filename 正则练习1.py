import re

# 写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'
for i in ['bat', 'bit', 'but', 'hat', 'hit', 'hut']:
    ret = re.match("[bh].[t]",i)
    print(ret.group(),end=' ')
    print(ret)
print()
print('*'*50)
# 163邮箱适配
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for i in email_list:
    ret = re.match('[\w]{4,20}@163\.com$', i)
    if ret:
        print(ret.group(), '是合法的163邮箱')
    else:
        print(i, '不是合法的163邮箱')
print('*'*50)

# 匹配0-99
ret = re.match("[1-9]?[0-9]$","08")
if ret:
    print("是0-99")
else:
    print('不是0-99')
