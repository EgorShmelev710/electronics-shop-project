from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, num_of_sim):
        super().__init__(name, price, quantity)
        self.num_of_sim = num_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.get_name}', {self.price}, {self.quantity}, {self.num_of_sim})"

    @property
    def number_of_sim(self):
        return self.num_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_of_sim):
        self.num_of_sim = num_of_sim
        if self.num_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
