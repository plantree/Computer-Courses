from socket import *
import random 
import time 

listenPort = 8080

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', listenPort))
# important, control heartbeat
serverSocket.settimeout(0.1)

startTime = float(time.time())
endTime = startTime

while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        message = message.decode()
        requestTime = float(message.split(' ')[1])
        endTime = requestTime
        rtt = float(time.time()) - requestTime
        print(message.split(' ')[0 ]+ ':', rtt)
    except Exception as e:
        if endTime == startTime:
            continue
        if time.time() - endTime >= 1.0:
            print('Heartbeat pause')
            break
        else:
            print('Packet lost')