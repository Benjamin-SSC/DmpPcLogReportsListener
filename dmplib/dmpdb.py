# pip install mysql-connector-python
import mysql.connector as db_module
import dmplib.dmputils as dmputils
import dmplib.dmpstaticdata as dmpstaticdata
import datetime
import ipaddress

# This is the singleton object to contain the DB object
class theDB(object):

    def __init__(self, dbauth:list):
        self.host = dbauth[0]
        self.user = dbauth[1]
        self.password = dbauth[2]
        self.database = dbauth[3]

        MIN_MYSQL = (8,0,32)
        if db_module.__version_info__ < MIN_MYSQL:
            print(f"WARNING! mysql-connector-python package may be too old!")
        self._db_connection = db_module.connect(
            host= self.host,
            user= self.user,
            password=self.password,
            database=self.database
            )
        self._db_cur = self._db_connection.cursor(dictionary=True)

    def query(self, query, params=None):
        return self._db_cur.execute(query, params)

    def __del__(self):
        self._db_connection.close()

def insertDbRecord(signaldict:dict, dbauth:list):

    # Get datetime of when the signal was set off
    signaltime = datetime.datetime.now() - datetime.timedelta(minutes=int(signaldict['minago']))
    dmputils.debugPrint(f"Signal was created at {signaltime}")

    # Convert the IP address to binary for storage in mysql
    fromip = ipaddress.ip_address(signaldict['ip'])
    if isinstance(fromip, ipaddress.IPv4Address):
        fromip = ipaddress.IPv6Address('::ffff:' + signaldict['ip'])
    elif isinstance(fromip, ipaddress.IPv6Address):
        pass
    else:
        print(f"Cannot Translate IP address: {signaldict['ip']}. Skipping.")
        return False

    db = theDB(dbauth)

    sql = (
            "INSERT INTO reportsignals "
            "( uuid, fromip, fromport, accountnumber, minutesago, signaltimestamp, rawmessage ) "
            "VALUES "
            "( %s, %s, %s, %s, %s, %s, %s )"
        )
    try:
        db._db_cur.execute(sql, (signaldict['uuid'], fromip.exploded, signaldict['port'], signaldict['acct'], signaldict['minago'], signaltime.strftime('%Y-%m-%d %H:%M:%S'), signaldict['rawmsg']))
        db._db_connection.commit()
        result = db._db_cur.fetchwarnings()
    except db_module.Error as err:
        print(f"Something went wrong!\n{err}")
        return False

    sql = (
        "INSERT INTO messages "
        "( uuid, fieldtype, qualifier, identifier, text ) "
        "VALUES "
        "( %s, %s, %s, %s, %s )"
    )

    try:
        for key in signaldict['msgdict']:
            if key in dmpstaticdata.field_ident_map:
                msglist = signaldict['msgdict'][key]
                for msg in msglist:
                    db._db_cur.execute(sql, (signaldict['uuid'], msg['fieldtype'], msg['qualifier'], msg['identifier'], msg['text']))
        db._db_connection.commit()
    except  db_module.Error as err:
        print(f"Something went wrong!\n{err}")
        return False

    return True

# EOF
