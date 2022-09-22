from socket import *
import time

serverAddr = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
# set timeout
clientSocket.settimeout(1)

for i in range(10):
    now = time.time()
    message = 'Ping {0} {1}'.format(i + 1, now)
    try:
        clientSocket.sendto(message.encode(), (serverAddr, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - now 
        print('Sequence {0}: Reply: {1}, RTT: {2}'.format(i + 1, modifiedMessage.decode(), rtt))
    except Exception as e:
        print('Sequence {0}: Request timeout'.format(i + 1))
