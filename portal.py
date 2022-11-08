class Portal:
    def __init__(self, name, company, mark):
        self.name = name
        self.company = company
        self.mark = mark

    def bulk_format(self):
        data_format = f'{self.name}|{self.company}|{self.mark}'
        return data_format