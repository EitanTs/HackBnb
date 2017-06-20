from Tables.Table import Table


class TableRooms(Table):

    TABLE_NAME = 'Rooms'

    def __init__(self, room_id, building, room_number, picture_path=None):
        super(TableRooms, self).__init__(self.TABLE_NAME)
        self.room_id = room_id
        self.building = building
        self.room_number = int(room_number)
        if picture_path:
            self.picture_path = picture_path
        else:
            self.picture_path = room_id

    @property
    def values(self):
        return self.room_id, self.building, self.room_number, self.picture_path

