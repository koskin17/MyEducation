class Cellphone:
    def __init__(self, manufact, model, retail_price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = retail_price

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

    def get_manufact(self):
        return 'Производитель телефона: ' + str(self.__manufact)

    def get_model(self):
        return 'Модель телефона: ' + str(self.__model)

    def get_retail_price(self):
        return 'Розничная цена телефона: ' + str(self.__retail_price)
        
        
        
