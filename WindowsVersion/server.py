import socket

HOST = ''
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

serversocket = socket.socket()
serversocket.bind(ADDR)

serversocket.listen(5)
while True:
	print('waiting for connection...')
	c, addr = serversocket.accept()
	print('connected from: ', addr)
	
	print('The server is ready to receive')
	while True:
		data = c.recv(BUFSIZ)
		if not data:
			break
		printtoscreen = 'From Client: %s' % (data.decode('utf-8'))
		print(printtoscreen)
		response = input('Server: ')
		c.send(response.encode('utf-8'))
	c.close()

serversocket.close()
