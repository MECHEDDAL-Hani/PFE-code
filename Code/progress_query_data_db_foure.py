""" Test DB Foure case with Sharding """

import subprocess
import time
from progress_query_data import SQLite
PATH = "/home/hani/dev/DB_Four/"

COMMAND = f'''
mongod -f "{PATH}CSRS/replication_1/DB_Four_CSRS_replication_1.conf"
mongod -f "{PATH}CSRS/replication_2/DB_Four_CSRS_replication_2.conf"
mongod -f "{PATH}CSRS/replication_3/DB_Four_CSRS_replication_3.conf"
mongod -f "{PATH}CSRS/replication_4/DB_Four_CSRS_replication_4.conf"

mongod -f "{PATH}shared_1/replication_1/DB_Four_shared_1_replication_1.conf"
mongod -f "{PATH}shared_1/replication_2/DB_Four_shared_1_replication_2.conf"
mongod -f "{PATH}shared_1/replication_3/DB_Four_shared_1_replication_3.conf"
mongod -f "{PATH}shared_1/replication_4/DB_Four_shared_1_replication_4.conf"

mongod -f "{PATH}shared_2/replication_1/DB_Four_shared_2_replication_1.conf"
mongod -f "{PATH}shared_2/replication_2/DB_Four_shared_2_replication_2.conf"
mongod -f "{PATH}shared_2/replication_3/DB_Four_shared_2_replication_3.conf"
mongod -f "{PATH}shared_2/replication_4/DB_Four_shared_2_replication_4.conf"

mongod -f "{PATH}shared_3/replication_1/DB_Four_shared_3_replication_1.conf"
mongod -f "{PATH}shared_3/replication_2/DB_Four_shared_3_replication_2.conf"
mongod -f "{PATH}shared_3/replication_3/DB_Four_shared_3_replication_3.conf"
mongod -f "{PATH}shared_3/replication_4/DB_Four_shared_3_replication_4.conf"

mongos -f "{PATH}Mongos/DB_Four_Mongos.conf"
'''


def test_db_foure():
    """ Test DB Three case with replication """

    data_base = SQLite(
        case="case 4",
        uri="mongodb://root:root@127.0.0.1:27070/?authSource=admin")

    data_base.run_test()


if __name__ == '__main__':

    subprocess.run(COMMAND, shell=True, check=True)
    time.sleep(120)

    test_db_foure()

    subprocess.run("killall mongos && killall mongod",
                   shell=True, check=True)
