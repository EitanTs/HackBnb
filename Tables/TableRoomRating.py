from Tables.Table import Table
from datetime import datetime


class TableRoomRating(Table):

    TABLE_NAME = 'RoomRating'
    DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'

    def __init__(self, room_id, param_key, param_value, user_id):
        super(TableRoomRating, self).__init__(self.TABLE_NAME)
        self.room_id = room_id
        self.param_key = param_key
        self.param_value = param_value
        self.user_id = user_id
        self.insertion_time = datetime.now().strftime(self.DATETIME_FORMAT)

    @property
    def values(self):
        return self.room_id, self.param_key, self.param_value, self.user_id, self.insertion_time

