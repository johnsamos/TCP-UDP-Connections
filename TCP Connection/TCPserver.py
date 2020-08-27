import socket as s
s.serverPort = 10000
s.serverSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
s.serverSocket.bind(('',s.serverPort))
s.serverSocket.listen(2)
print('The server is ready to receive')


while 1:
    connectionSocket, addr = s.serverSocket.accept()
    message = connectionSocket.recv(1024)
    connectionSocket.send(message)
    connectionSocket.send(message)

    connectionSocket.close()