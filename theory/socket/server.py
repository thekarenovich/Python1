import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))

server.listen()

while True:
	user, adres = server.accept()

	print('connect')
	user.send('connect'.encode('utf-8'))
