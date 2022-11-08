class Advertisement:
    def __init__(self, id, service_id, salon_id, advertiser_id, type, price):
        self.id = id
        self.service_id = service_id
        self.salon_id = salon_id
        self.advertiser_id = advertiser_id
        self.type = type
        self.price = price

    def bulk_format(self):
        data_format = f'{self.id}|{self.service_id}|{self.salon_id}|{self.advertiser_id}|{self.type}|'\
                        f'{self.price}'
        return data_format