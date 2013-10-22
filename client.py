#!/usr/bin/env python
import socket

# gets host name, size and port
HOST = '127.0.0.1'
PORT = 12345
BUFSIZ = 1024
# creates address using host(localhost) and port
ADDR = (HOST, PORT)

# creates socket 
s = socket.socket()
# connects socket using addr from above
s.connect(ADDR)

while True:
	# while connected, grab input from client
	data = raw_input('Client: ')
	# if its not data, like a blank
	if not data:
		break # break out of the loop
	# otherwise send the input to the server
	s.send(data.encode('utf-8'))

	# waits and receives info from server
	data = s.recv(BUFSIZ)

	if not data:# if its a blank
		break #break out of loop

	# print server message to screen
	printtoscreen = 'From Server: %s' % (data.decode('utf-8'))
	print(printtoscreen)

s.close
