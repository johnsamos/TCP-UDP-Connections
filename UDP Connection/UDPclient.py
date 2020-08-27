import socket as s

s.serverName = '127.0.0.1' # Add your server ip address
s.serverPort = 10000
s.clientSocket = s.socket(s.AF_INET, s.SOCK_DGRAM)
message = input('input lowercase sentence:')
s.clientSocket.sendto(message.encode('utf-8'), (s.serverName, s.serverPort))
modifiedMessage, serverAddress = s.clientSocket.recvfrom(2048)
print(modifiedMessage)
s.clientSocket.close()
