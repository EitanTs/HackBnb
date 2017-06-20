from Tables.Table import Table


class TablePreferences(Table):

    TABLE_NAME = 'Preferences'

    def __init__(self, user_id, param_key, param_value):
        super(TablePreferences, self).__init__(self.TABLE_NAME)
        self.user_id = user_id
        self.param_key = param_key
        self.param_value = param_value

    @property
    def values(self):
        return self.user_id, self.param_key, self.param_value

