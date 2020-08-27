import socket as s

s.serverPort = 10000
s.serverSocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
s.serverSocket.bind(('', s.serverPort))
print('The server is ready to receive!')
while 1:
    message, clientAdress = s.serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    s.serverSocket.sendto(modifiedMessage, clientAdress)