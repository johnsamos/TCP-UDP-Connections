import socket as s
s.serverName = '127.0.0.1' # Add your server ip address
s.serverPort = 10000
s.clientSocket = s.socket(s.AF_INET, s.SOCK_STREAM)
s.clientSocket.connect((s.serverName, s.serverPort))
sentence = input('input lowcase sentence:')
s.clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = s.clientSocket.recv(1024)
print('From Server: ', modifiedSentence)
s.clientSocket.close()
