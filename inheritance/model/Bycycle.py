from overrides import overrides

from inheritance.model.Vehicle import Vehicle


class Bycycle(Vehicle):
    model_name = 'BMX'

    def __init__(self, brand, model_name):
        super().__init__(brand)
        self.model_name = model_name

    @overrides
    def honk(self):
        print("Bit bit!")
