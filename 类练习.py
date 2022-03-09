# 完成类属性，类方法的使用（和上课保持一致即可）
class Tools:
    count = 0
    def __init__(self,name):
        self.name = name
        Tools.count += 1

    @classmethod
    def show_tools(cls):
        print('有{}个工具'.format(cls.count))

chuizi = Tools('chuizi')
futou = Tools('futou')
Tools.show_tools()


