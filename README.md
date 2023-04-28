# DmpPcLogReportsListener

This program will listen on the specified IP address and TCP port, capture events from DMP panels via it's PC Log Reports feature, and save them to a MariaDB/Mysql database.

The PC Reports connection is seperate from the conneciton the panel uses to report signals to alarm receivers and central
stations. In the case of the log server (this software) being inaccessable, the panel will cache up to 65535 events and send them when the connection is reestablished.

This program requires a relitively new python mysql-connector-python module, and a MariaDB/Mysql server version new enough to be able to use UUID fields.

The latest of each is recommended.

This program is licenced under the GNU General Public License v3.

***THIS PROGRAM IS NOT DESIGNED TO BE USED FOR MONITORING LIFE SAFETY SIGNALS***

***IT IS NOT SAFE TO USE THIS PROGRAM FOR ACTING ON LIFE SAFETY SIGNALS***

***USE A PROPERLY UL LISTED CENTRAL STATION STAFFED BY PROFESSIONALS FOR LIFE SAFETY SIGNALS***

```
usage: dmplistener [-h] [-L LISTEN_IP] [-T LISTEN_PORT] [-H DB_HOST] [-D DB_DATABASE] [-U DB_USER] [-P DB_PASSWORD] [--debug]

Listens via TCP port for DMP panels to connect with PC Log Reports.
These are saved to a MariaDB/MySql database.
See the schema.sql file in the source distribution for the table schema.

options:
  -h, --help            show this help message and exit
  -L LISTEN_IP, --listenaddr LISTEN_IP
                        The IP address to listen on. Default: 0.0.0.0 [all]
  -T LISTEN_PORT, --tcpport LISTEN_PORT
                        The TCP Port to listen on. Default: 2001
  -H DB_HOST, --db-host DB_HOST
                        The host/ip of the MariaDB/Mysql server
  -D DB_DATABASE, --db_databse DB_DATABASE
                        The database to use when connecting to the MariaDB/Mysql server
  -U DB_USER, --db_user DB_USER
                        The username to use when connecting to the MariaDB/Mysql server
  -P DB_PASSWORD, --db-password DB_PASSWORD
                        The password to use when connecting to the MariaDB/Mysql server
  --debug               Turns on Debug messages

These settings can also be set via environment variables, as listed in capital letters above.

Examples:
./dmplistener -L 192.168.1.122 -T 2002 -H 192.168.1.100 -D dmpreports2 -U myuser -P mypassword
LISTEN_IP=192.168.1.122 LISTEN_PORT=2002 DB_HOST=192.168.1.100 DB_DATABASE=dmpreports2 DB_USER=myuser DB_PASSWORD=mypassword ./dmplistener
DEBUG=TRUE ./dmplistener
```

