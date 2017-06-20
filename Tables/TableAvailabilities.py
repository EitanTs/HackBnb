from Tables.Table import Table


class TableAvailabilities(Table):

    TABLE_NAME = 'Availabilities'

    def __init__(self, bed_id, date, user_id, renter_id=None):
        super(TableAvailabilities, self).__init__(self.TABLE_NAME)
        self.bed_id = bed_id
        self.date = date
        self.user_id = user_id
        self.renter_id = renter_id

    @property
    def values(self):
        return self.bed_id, self.date, self.user_id, self.renter_id

