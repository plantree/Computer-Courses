from audioop import avg
from socket import *
import time
from traceback import print_tb

serverAddr = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
# set timeout
clientSocket.settimeout(1)

# store RTT
succRequests = []

for i in range(10):
    now = time.time()
    message = 'Ping {0} {1}'.format(i + 1, now)
    try:
        clientSocket.sendto(message.encode(), (serverAddr, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rtt = time.time() - now 
        succRequests.append(rtt)
        print('Sequence {0}: Reply: {1}, RTT: {2}'.format(i + 1, modifiedMessage.decode(), rtt))
    except Exception as e:
        print('Sequence {0}: Request timeout'.format(i + 1))
print('Send 10 requests. Success Rate: {0}%, Min RTT: {1}, Max RTT: {2}, Avg RTT: {3}'.format(len(succRequests) / 10 * 100, min(succRequests), max(succRequests), sum(succRequests)/ len(succRequests)))