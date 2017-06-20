from Tables.Table import Table


class TableBeds(Table):

    TABLE_NAME = 'Beds'

    def __init__(self, bed_id, user_id, bed_number, room_id, description):
        super(TableBeds, self).__init__(self.TABLE_NAME)
        self.bed_id = bed_id
        self.user_id = user_id
        self.bed_number = bed_number
        self.room_id = room_id
        self.description = description

    @property
    def values(self):
        return self.bed_id, self.user_id, self.room_id, self.bed_number, self.description

