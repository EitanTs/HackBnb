__author__ = 'Ido Bichler'

from DB.Queries import SelectQueries
from DB.SqlExecuter import SqlExecuter

class LoginManager(object):
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    def is_valid(self):
        query = SelectQueries.VALIDE_USER_AND_PASSWORD.format(user_id=self.user_id, password=self.password)
        exists = SqlExecuter().get_table_content_as_json(query)[0]['valid']
        return bool(exists)