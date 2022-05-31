""" SQLite database operations """
import sqlite3
from sqlite3 import Error
from mongodb import Mongodb


class SQLite:
    """handel sqlite database"""

    def __init__(self,
                 case="case",
                 uri="mongodb://root:root@127.0.0.1:27010/myDB?authSource=admin",
                 connection=r"db.db",
                 machine="Machine Hani Linux",
                 data_base="myDB"
                 ):

        self.connection = SQLite.create_connection_sqlite(connection)
        self.create_results_table()
        self.machine = machine
        self.case = case
        self.mongodb = Mongodb(uri, data_base)

    @staticmethod
    def create_connection_sqlite(db_file):
        """ create a database connection to a SQLite database """

        connection = None
        try:
            connection = sqlite3.connect(db_file)
            return connection
        except Error as error:
            print(error)
            return connection

    def create_results_table(self):
        """ Create results table """

        try:
            sql_create_results_table = """CREATE TABLE IF NOT EXISTS "results" (
                                            "id" INTEGER,
                                            "queryy" TEXT,
                                            "time" INTEGER,
                                            "number_documents_returned" INTEGER,
                                            "ixscan" INTEGER,
                                            "index_keys_examined" INTEGER,
                                            "fetch" INTEGER,
                                            "documents_examined" TEXT,
                                            "machine" TEXT,
                                            "casee" TEXT,
                                            PRIMARY KEY("id" AUTOINCREMENT)
                                        );"""
            cursor = self.connection.cursor()
            cursor.execute(sql_create_results_table)
        except Error as error:
            print(error)

    def insert_result(self, result):
        """ insert result """

        try:
            sql_insert_result = """ INSERT INTO "results"
                ("queryy",
                "time",
                "number_documents_returned",
                "ixscan",
                "index_keys_examined",
                "fetch",
                "documents_examined",
                "machine",
                "casee")
                VALUES(?,?,?,?,?,?,?,?,?);"""
            cursor = self.connection.cursor()
            cursor.execute(sql_insert_result, result)
            self.connection.commit()
            return 1
        except Error as error:
            print(error)
            return 0

    def select_avg_result(self, query, case, machine="Machine Hani Linux"):
        """select all result of a query and machine and return avg time"""

        cursor = self.connection.cursor()
        sql_select_result = f"""SELECT
                                avg(time)
                            FROM
                                results
                            WHERE
                                results.queryy = "{query}"
                            AND
                                results.casee = "{case}"
                            AND
                                results.machine = "{machine}";
                                """
        # print(sql_select_result)
        cursor.execute(sql_select_result)
        rows = cursor.fetchone()

        return rows[0]

    def advance_query_one(self):
        """ Docstring """
        table_result = self.mongodb.query_one()
        result = ["Query 1",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_two(self):
        """ Docstring """

        table_result = self.mongodb.query_two()
        result = ["Query 2",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_three(self):
        """ Docstring """

        table_result = self.mongodb.query_three()
        result = ["Query 3",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_four(self):
        """ Docstring """

        table_result = self.mongodb.query_four()
        result = ["Query 4",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_five(self):
        """ Docstring """

        table_result = self.mongodb.query_five()
        result = ["Query 5",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_six(self):
        """ Docstring """

        table_result = self.mongodb.query_six()
        result = ["Query 6",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_seven(self):
        """ Docstring """

        table_result = self.mongodb.query_seven()
        result = ["Query 7",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_eight(self):
        """ Docstring """

        table_result = self.mongodb.query_eight()
        result = ["Query 8",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_nine(self):
        """ Docstring """

        table_result = self.mongodb.query_nine()
        result = ["Query 9",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_ten(self):
        """ Docstring """

        table_result = self.mongodb.query_ten()
        result = ["Query 10",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_eleven(self):
        """ Docstring """

        table_result = self.mongodb.query_eleven()
        result = ["Query 11",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_twelve(self):
        """ Docstring """

        table_result = self.mongodb.query_twelve()
        result = ["Query 12",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_thirteen(self):
        """ Docstring """

        table_result = self.mongodb.query_thirteen()
        result = ["Query 13",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def advance_query_fourteen(self):
        """ Docstring """

        table_result = self.mongodb.query_fourteen()
        result = ["Query 14",
                  table_result[0],
                  table_result[1],
                  table_result[2],
                  table_result[3],
                  table_result[4],
                  table_result[5],
                  self.machine,
                  self.case]
        self.insert_result(result)

    def run_test(self, number_time=20):
        """run progress"""

        for time in range(number_time):

            self.advance_query_one()
            print(f"Query 1 : {time}")

            self.advance_query_two()
            print(f"Query 2 : {time}")

            self.advance_query_three()
            print(f"Query 3 : {time}")

            self.advance_query_four()
            print(f"Query 4 : {time}")

            self.advance_query_five()
            print(f"Query 5 : {time}")

            self.advance_query_six()
            print(f"Query 6 : {time}")

            self.advance_query_seven()
            print(f"Query 7 : {time}")

            self.advance_query_eight()
            print(f"Query 8 : {time}")

            self.advance_query_nine()
            print(f"Query 9 : {time}")

            self.advance_query_ten()
            print(f"Query 10 : {time}")

            self.advance_query_eleven()
            print(f"Query 11 : {time}")

            self.advance_query_twelve()
            print(f"Query 12 : {time}")

            self.advance_query_thirteen()
            print(f"Query 13 : {time}")

            self.advance_query_fourteen()
            print(f"Query 14 : {time}")

    def run_test_two(self, number_time=20):
        """ Docstring """
        for time in range(number_time):

            self.advance_query_one()
            print(f"Query 1 : {time}")

            self.advance_query_two()
            print(f"Query 2 : {time}")

            self.advance_query_three()
            print(f"Query 3 : {time}")

            self.advance_query_four()
            print(f"Query 4 : {time}")

            self.advance_query_five()
            print(f"Query 5 : {time}")

            self.advance_query_six()
            print(f"Query 6 : {time}")

            self.advance_query_seven()
            print(f"Query 7 : {time}")

            self.advance_query_eight()
            print(f"Query 8 : {time}")


if __name__ == '__main__':
    # sqLite = SQLite()
    # # sqLite.insert_result(["select all data", 300, "machine hani"])
    # # sqLite.insert_result(["select all data", 600, "machine hani"])
    # # print(sqLite.select_avg_result("select all data", "machine hani"))
    # # # main()
    # sqLite.run_test()
    # SQLite("case 4", "mongodb://root:root@127.0.0.1:27070/?authSource=admin").advance_query_one()
    pass
