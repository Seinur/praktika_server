import socket
import psycopg2
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        break
    text = data.decode('utf-8')
    login=text[:text.find('\n')]
    password = text[text.find('\n')+1:]
    con = psycopg2.connect(dbname='postgres', user='postgres',
                           password='058066', host='localhost')
   
    cur = con.cursor()
    cur.execute("SELECT login, pass from DATA")

    rows = cur.fetchall()
    for row in rows:

        if(row[0]==login and row[1]==password):
            res=1
            conn.send("Вы успешно вошли".encode('utf-8'))
            break
        else: res=0
    if(res==0):
        conn.send("Неправильно введен логин или пароль".encode('utf-8'))

    con.close()



conn.close()