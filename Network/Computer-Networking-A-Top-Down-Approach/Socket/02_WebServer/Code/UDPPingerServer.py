# we will need the following module to generate randomized lost packets
import random
from socket import *

listenPort = 12000

# create a UDP socket 
# notice the use of SOCK_DGRAM fro UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# assign IP address and port number to socket 
serverSocket.bind(('', listenPort))

while True:
    # generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # capitalize the message from the client
    message = message.upper()
    # if rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # otherwise, the server responds
    serverSocket.sendto(message, address)