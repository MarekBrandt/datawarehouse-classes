class Company:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def bulk_format(self):
        data_format = f'{self.name}|{self.specialization}'
        return data_format