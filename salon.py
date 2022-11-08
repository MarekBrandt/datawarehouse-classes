class Salon:
    def __init__(self, id, city, street, building_number, phone_number):
        self.id = id
        self.city = city
        self.street = street
        self.building_number = building_number
        self.phone_number = phone_number


    def bulk_format(self):
        data_format = f'{self.id}|{self.city}|{self.street}|{self.building_number}|{self.phone_number}|'
        return data_format