class Customer:
    def __init__(self, id, name, surname, birth_year):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth_year = birth_year



    def bulk_format(self):
        data_format = f'{self.id}|{self.name}|{self.surname}|{self.birth_year}'
        return data_format