from DB.SqlExecuter import SqlExecuter
from Tables.TableRoomRating import TableRoomRating


def test_sanity():
    table_users = TableRoomRating(room_id='1111', param_key='snorks', param_value='3', user_id='Eitan')
    SqlExecuter().execute_query(table_users.generate_insert_query(), table_users.values)


if __name__ == '__main__':
    test_sanity()
