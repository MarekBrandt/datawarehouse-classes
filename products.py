class Product:
    def __init__(self, id, name, brand, type, price):
        self.id = id
        self.name = name
        self.brand = brand
        self.type = type
        self.price = price

    def bulk_format(self):
        data_format = f'{self.id}|{self.name}|{self.brand}|{self.type}|{self.price}'
        return data_format
