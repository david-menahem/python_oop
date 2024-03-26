from overrides import overrides

from inheritance.chair.Chair import Chair


# Duplicate subclass attributes for inheritance practice
class KitchenChair(Chair):
    def __init__(self, model, number_of_legs, price, is_spinning, is_adjustable, has_discount, discount):
        super().__init__(model, number_of_legs, price)
        self.__is_spinning = is_spinning
        self.__is_adjustable = is_adjustable
        self.__has_discount = has_discount
        self.__discount = discount

    @property
    def is_spinning(self):
        return self.__is_spinning

    @is_spinning.setter
    def is_spinning(self, is_spinning):
        self.__is_spinning = is_spinning

    @property
    def is_adjustable(self):
        return self.__is_adjustable

    @is_adjustable.setter
    def is_adjustable(self, is_adjustable):
        self.__is_adjustable = is_adjustable

    @property
    def has_discount(self):
        return self.__has_discount

    @has_discount.setter
    def has_discount(self, has_discount):
        self.__has_discount = has_discount

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount

    @overrides
    def print_chair(self):
        super().print_chair()
        print(f'Is spinning?: {self.__is_spinning}, Is Adjustable?: {self.__is_adjustable},'
              f' Has discount? {self.__has_discount}, Discount: %{self.__discount}')

    @overrides
    def calculate_price(self, number_of_chairs):
        if self.__has_discount:
            return number_of_chairs * self.price * (100 - self.__discount) / 100
        else:
            return super().calculate_price(number_of_chairs)
