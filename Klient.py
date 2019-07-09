import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

login = input("Введите логин : ");
password = input("Введите пароль : ");
text3=str(str(login)+'\n'+str(password))
sock.send(str(str(login)+'\n'+str(password)).encode('utf-8'))
##string = 'hello, world!'
##sock.send(string.encode('utf-8'))
#print(text3[text3.find('\n'):])

#sock.send(text.encode('utf-8'))
data = sock.recv(1024)
sock.close()
print(data.decode("utf-8"))




