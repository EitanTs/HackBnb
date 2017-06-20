from DB.SqlExecuter import SqlExecuter


class Table(object):
    INSERT_QUERY = 'INSERT INTO {table_name} VALUES ({params_format})'
    IS_EXIST_QUERY = "SELECT * FROM {table_name} WHERE {column_key}='{column_value}'"
    PARAM = '?,'

    def __init__(self, table_name):
        self.table_name = table_name

    def generate_insert_query(self):
        params_format = ''
        for i in xrange(len(self.values)):
            params_format += self.PARAM
        params_format = params_format[:-1]
        return self.INSERT_QUERY.format(table_name=self.table_name, params_format=params_format)

    def is_exist(self, key, value, query=None):
        if not query:
            return bool(len(
                SqlExecuter().get_table_content_as_json(
                    self.IS_EXIST_QUERY.format(table_name=self.table_name, column_key=key, column_value=value))))
        return bool(len(
                    SqlExecuter().get_table_content_as_json(query)))