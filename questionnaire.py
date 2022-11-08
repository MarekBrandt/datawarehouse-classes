class Questionnaire:
    def __init__(self, ad_id, ad_is_cause, ad_seen, points, visit_id):
        self.ad_id = ad_id
        self.ad_is_cause = ad_is_cause
        self.ad_seen = ad_seen
        self.points = points
        self.visit_id = visit_id

    def csv_format(self):
        data_format = f'{self.ad_id},{self.ad_is_cause},{self.ad_seen},{self.points},' \
                      f'{self.visit_id}'
        return data_format
