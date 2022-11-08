class Service:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def bulk_format(self):
        data_format = f'{self.id}|{self.name}|{self.price}'
        return data_format
