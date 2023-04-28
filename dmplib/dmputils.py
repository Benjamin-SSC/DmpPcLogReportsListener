### Utility Functions ###
import os
import mysql.connector
from mysql.connector import Error

# Print to stdout if Debugging is enabled.
def debugPrint(printthis):

    if os.getenv("DMPDEBUG"):
        print(f"D: {printthis}")


def testDbConnection(host:str, db:str, user:str, passwd:str):
    MIN_MYSQL = (8,0,32)
    if mysql.connector.__version_info__ < MIN_MYSQL:
        print(f"WARNING! mysql-connector-python package may be too old!")

    conn = None
    try:
        conn = mysql.connector.connect(host=host,
                                        database=db,
                                        user=user,
                                        password=passwd)
        if conn.is_connected():
            debugPrint("DB Test Successful")
            return True

    except Error as e:
        print(e)
        return False

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

# EOF
