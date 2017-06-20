__author__ = 'Ido Bichler'
from DB.Queries import SelectQueries
from DB.SqlExecuter import SqlExecuter

class RentUser(object):
    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def preferences_query(self):
        return SelectQueries.USER_PREFRENCES.format(user_id=self.user_id)

    def get_preferences(self):
        preferences_json = SqlExecuter().get_table_content_as_json(self.preferences_query)
        preferences_dict = {}
        for row in preferences_json:
            key = row["ParamKey"]
            value = row["ParamValue"]
            preferences_dict[key] = value
        return preferences_dict
