#!/usr/bin/env python
import socket

# gets host name, port num and buff size
HOST = ''
PORT = 12345
BUFSIZ = 1024
# creates address with hostname and port
ADDR = (HOST, PORT)

# creates socket
serversocket = socket.socket()
# binds the socket to the address (server size)
serversocket.bind(ADDR)
# have the server listen
serversocket.listen(5)

while True: # while connection is open
	# wait for a connection
	print('waiting for connection...')
	# when it is accepted, add value to c and addr
	c, addr = serversocket.accept()
	print('connected from: ', addr)

	# alert the server is ready
	print('The server is ready to receive')

	while True: # while connection to socket is value
		# receive value from client
		data = c.recv(BUFSIZ)

		if not data: # if its a blank
			break # break out of loop
		# print client string to terminal
		printtoscreen = 'From Client: %s' % (data.decode('utf-8'))
		print(printtoscreen)
		
		# get response from server
		response = raw_input('Server: ')
		c.send(response.encode('utf-8'))
	# when client closes, close the client socket
	c.close()
# close server socket
serversocket.close()
