from Tables.Table import Table


class TableUsers(Table):

    TABLE_NAME = 'Users'

    def __init__(self, user_id, password, first_name, last_name, phone_number, voip, is_owner):
        super(TableUsers, self).__init__(self.TABLE_NAME)
        self.user_id = user_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.voip = voip
        if is_owner:
            self.is_owner = True
        else:
            self.is_owner = False



    @property
    def values(self):
        return self.user_id, self.password, self.first_name, self.last_name, self.phone_number, self.voip, self.is_owner

