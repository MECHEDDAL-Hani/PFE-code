""" Test DB Three case with replication """

import subprocess
import time
from progress_query_data import SQLite

URI1 = "127.0.0.1:27020"
URI2 = "127.0.0.1:27021"
URI3 = "127.0.0.1:27022"
URI4 = "127.0.0.1:27023"
REPL = "replicaSet=my_replication"
UP = "root:root"
URI = f"mongodb://{UP}@{URI1},{URI2},{URI3},{URI4}/?{REPL}&authSource=admin"

COMMAND = '''
mongod -f "/home/hani/dev/DB_Three/primary/DB_Three.conf"
mongod -f "/home/hani/dev/DB_Three/replication_1/DB_Three_replication_1.conf"
mongod -f "/home/hani/dev/DB_Three/replication_2/DB_Three_replication_2.conf"
mongod -f "/home/hani/dev/DB_Three/replication_3/DB_Three_replication_3.conf"
'''


def test_db_three():
    """ Test DB Three case with replication """

    data_base = SQLite(
        case="case 3",
        uri=URI)

    data_base.run_test()


if __name__ == '__main__':

    subprocess.run(COMMAND, shell=True, check=True)
    time.sleep(30)

    test_db_three()

    subprocess.run("killall mongod", shell=True, check=True)
