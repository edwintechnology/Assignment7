import socket

HOST = '127.0.0.1'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

s = socket.socket()
s.connect(ADDR)

while True:
	data = input('Client: ')
	if not data:
		break
	s.send(data.encode('utf-8'))
	data = s.recv(BUFSIZ)
	if not data:
		break
	printtoscreen = 'From Server %s' % (data.decode('utf-8'))
	print(printtoscreen)

s.close
