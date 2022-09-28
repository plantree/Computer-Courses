from socket import *
import time 

serverAddr = '127.0.0.1'
serverPort = 8080

clientSockt = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    requestTime = time.time()
    message = '{0} {1}'.format(i + 1, requestTime)
    clientSockt.sendto(message.encode(), (serverAddr, serverPort))
clientSockt.close()  