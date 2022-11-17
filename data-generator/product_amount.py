class ProductAmount:
    def __init__(self, visit_id, product_id, amount):
        self.visit_id = visit_id
        self.product_id = product_id
        self.amount = amount

    def bulk_format(self):
        data_format = f'{self.visit_id}|{self.product_id}|{self.amount}'
        return data_format
