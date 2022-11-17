class ServiceVisit:
    def __init__(self, visit_id, service_id):
        self.visit_id = visit_id
        self.service_id = service_id

    def bulk_format(self):
        data_format = f'{self.service_id}|{self.visit_id}'
        return data_format
