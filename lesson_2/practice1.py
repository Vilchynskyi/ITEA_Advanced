if __name__ == '__main__':
    class Shop:
        total_goods_sold = 0

        def __init__(self, name_of_shop, goods_sold):
            self.name_of_shop = name_of_shop
            self.goods_sold = goods_sold
            Shop.total_goods_sold += goods_sold

        def increase_the_number_of_goods_sold(self, goods_sold):
            Shop.total_goods_sold += goods_sold

        def get_total_goods_sold():
            return Shop.total_goods_sold


    atb = Shop('ATB', 2000)
    fora = Shop('Fora', 1000)
    atb.increase_the_number_of_goods_sold(100)
    print('Total goods sold by all shops -', Shop.get_total_goods_sold())
