import socket
import postgresql
import psycopg2
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
   ## db = postgresql.open('mydb.db')
    con = None

    try:

        con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='password'")
        cur = con.cursor()
        cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
        cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
        cur.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
        cur.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
        cur.execute("INSERT INTO Products VALUES(4,'Bread',5)")
        cur.execute("INSERT INTO Products VALUES(5,'Oranges',3)")

        con.commit()
        print(con)
    except (psycopg2.DatabaseError, e):
        if con:
            con.rollback()

        print
        ('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()

    conn.send(con)

conn.close()