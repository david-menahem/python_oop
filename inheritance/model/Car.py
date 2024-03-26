from overrides import overrides

from inheritance.model.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model_name):
        super().__init__(brand)
        self.model_name = model_name

    @overrides
    def honk(self):
        super().honk()
        print('beep beep!')
