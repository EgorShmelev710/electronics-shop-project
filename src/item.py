import csv


class InstantiateCSVError(Exception):
    pass

    # def __init__(self, *args, **kwargs):
    #     self.message = 'Файл item.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

        super().__init__()

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, data_string):
        self.name = data_string[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path, newline='', encoding='cp1251') as csvfile:
                cls.all.clear()
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] is None or row['price'] is None or row['quantity'] is None:
                        raise InstantiateCSVError('Файл item.csv поврежден')

                    else:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
            raise FileNotFoundError

    @staticmethod
    def string_to_number(string):
        return int(float(string))
