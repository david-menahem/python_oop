class Item:
    def __init__(self,name,price,category,amount,weight):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__amount = amount
        self.__weight = weight

    def print_item(self,item):
        print(f'Item name: {item.name}, Item price: {item.price} NIS, Item category: {item.category}'
              f' Item amount: {item.amount}, Item weight: {item.weight} kg')
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight
