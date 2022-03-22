class Goods():

    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount

    @property
    def dis_price(self):
        return self.price *self.discount

if __name__ == '__main__':
    goods = Goods('fish',10,0.8)
    print(goods.dis_price)

