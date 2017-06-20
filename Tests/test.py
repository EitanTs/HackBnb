__author__ = 'Ido Bichler'

from Manager.BedManager import BedManager
from Manager.LoginManager import LoginManager
from DB.SqlExecuter import SqlExecuter
from Tables.TableAvailabilities import TableAvailabilities
from DB.Queries import UpdeteQueries

def test_sanity():
    update_query = UpdeteQueries.UPDATE_AVIBILITIES.format(user_id='tommm', bed_id='A_123_1', check_in='12-06-2017')
    SqlExecuter().execute_query(update_query)

if __name__ == '__main__':
    test_sanity()