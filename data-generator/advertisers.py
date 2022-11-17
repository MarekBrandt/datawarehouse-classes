class Advertiser:
    def __init__(self, id, email, name, nip, specialization, thematic):
        self.id = id
        self.email = email
        self.name = name
        self.nip = nip
        self.specialization = specialization
        self.thematic = thematic

    def bulk_format(self):
        data_format = f'{self.id}|{self.email}|{self.name}|{self.nip}|{self.specialization}|{self.thematic}'
        return data_format
