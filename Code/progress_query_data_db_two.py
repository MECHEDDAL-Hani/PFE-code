""" Test DB Two case with index """

import subprocess
import time
from progress_query_data import SQLite


def test_db_two():
    """ Test DB Two case with index """

    data_base = SQLite(
        case="case 2",
        uri="mongodb://root:root@127.0.0.1:27010/?authSource=admin")

    data_base.run_test()


if __name__ == '__main__':

    subprocess.run('mongod -f "/home/hani/dev/DB_Two/DB_Two.conf"',
                   shell=True, check=True)
    time.sleep(30)

    test_db_two()

    subprocess.run("killall mongod", shell=True, check=True)
