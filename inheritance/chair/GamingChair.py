from overrides import overrides

from inheritance.chair.Chair import Chair
from inheritance.chair.Parts import Parts


# Duplicate subclass attributes for inheritance practice
class GamingChair(Chair):
    def __init__(self, model, number_of_legs, price, is_spinning, is_adjustable, has_discount, discount, parts : Parts):
        super().__init__(model, number_of_legs, price)
        self.__is_spinning = is_spinning
        self.__is_adjustable = is_adjustable
        self.__has_discount = has_discount
        self.__discount = discount
        self.__parts = parts

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

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, parts):
        self.__parts = parts

    @overrides
    def print_chair(self):
        super().print_chair()
        print(f'Is spinning?: {self.__is_spinning}, Is Adjustable?: {self.__is_adjustable},'
              f' Has discount? {self.__has_discount}, Discount: {self.__discount}% ')
        print(f'Parts: Screws: {self.__parts.screws}, Fabric: {self.__parts.fabric}')

    @overrides
    def calculate_price(self, number_of_chairs):
        if self.__has_discount:
            return number_of_chairs * self.price * (100 - self.__discount) / 100
        else:
            return super().calculate_price(number_of_chairs)
