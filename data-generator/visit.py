class Visit:
    def __init__(self, id, salon_id, customer_id, reservation_date, visit_date, cancellation_date, amount):
        self.id = id
        self.salon_id = salon_id
        self.customer_id = customer_id
        self.reservation_date = reservation_date
        self.visit_date = visit_date
        self.cancellation_date = cancellation_date
        self.amount = amount

    def bulk_format(self):
        data_format = f'{self.id}|{self.salon_id}|{self.customer_id}|{self.reservation_date}|{self.visit_date}|{self.cancellation_date}|{self.amount}'
        return data_format
