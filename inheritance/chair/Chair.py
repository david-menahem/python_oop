class Chair:
    def __init__(self,model,number_of_legs,price):
        self.__model = model
        self.__number_of_legs = number_of_legs
        self.__price = price

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,model):
        self.__model = model

    @property
    def number_of_legs(self):
        return self.__number_of_legs

    @number_of_legs.setter
    def number_of_legs(self, number_of_legs):
        self.__number_of_legs = number_of_legs

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def print_chair(self):
        print(f'Model: {self.__model}, Number of legs: {self.__number_of_legs}, Price: {self.__price}')

    def calculate_price(self,number_of_chairs):
        return number_of_chairs * self.__price