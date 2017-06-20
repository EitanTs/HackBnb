import sqlite3
from DB.Configuration import DbConfiguration


class SqlExecuter(DbConfiguration):
    def __init__(self):
        super(SqlExecuter, self).__init__()

    def get_table_content_as_json(self, query, params=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if params:
                if not isinstance(params, list):
                    raise TypeError("Expected list not {0}".format(type(params)))
                cursor.execute(query.format(*params))
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
        return self._convert_table_to_json(rows, self._get_cols(cursor.description))

    def execute_query(self, query, params=None, is_many=False):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if is_many:
                cursor.executemany(query, params)
            else:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            conn.commit()

    @staticmethod
    def _get_cols(description):
        cols = []
        for col_description in description:
            cols.append(col_description[0])
        return cols

    @staticmethod
    def _convert_table_to_json(rows, cols):
        json_array = []
        for row in rows:
            row_json = {}
            for i in xrange(len(cols)):
                row_json[cols[i]] = row[i]
            json_array.append(row_json)
        return json_array

    def insert_object_to_db(self, table_obj):
        self.execute_query(table_obj.generate_insert_query(), table_obj.values)