import os


class DbConfiguration(object):
    def __init__(self):
        self._db_name = 'AirBnb.db'

    @property
    def db_path(self):
        return os.path.join(os.path.dirname(__file__), self._db_name)
