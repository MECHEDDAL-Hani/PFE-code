""" Test DB One case without index """

import subprocess
import time
from progress_query_data import SQLite


def test_db_one():
    """ Test DB One case without index """
    data_base = SQLite(
        "case 1",
        "mongodb://root:root@127.0.0.1:27001/?authSource=admin")

    data_base.run_test_two()


if __name__ == '__main__':

    subprocess.run('mongod -f "/home/hani/dev/DB_One/DB_One.conf"',
                   shell=True, check=True)
    time.sleep(30)

    test_db_one()

    subprocess.run("killall mongod", shell=True, check=True)
