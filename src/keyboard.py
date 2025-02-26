from src.item import Item


class Lang:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language.upper() not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self.__language = language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Item, Lang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
