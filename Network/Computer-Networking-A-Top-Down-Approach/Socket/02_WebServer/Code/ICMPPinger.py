from datetime import timedelta
from socket import *
import os 
import sys
import struct 
import time 
import select 
import binascii
from zlib import DEFLATED

ICMP_ECHO_REQUEST = 8

def checksum(string):
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0 

    while count < countTo:
        thisVal = ord(string[count + 1]) * 256 + ord(string[count])
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2 

    if countTo < len(string):
        csum = csum + ord(string[len(string) - 1])
        csum = csum & 0xffffffff
    
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum 
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout 

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # timeout 
            return 'Request timed out'

        timeReveived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # fetch the ICMP header from the IP packet 
        header = recPacket[20:28]
        type, code, checksum, packetID, seq = struct.unpack('!bbHHh', header)
        if type == 0 and packetID == ID:    # tyoe should be 0
            byteInDouble = struct.calcsize('!d')
            timeSent = struct.unpack('!d', recPacket[28:28 + byteInDouble])[0]
            delay = timeReveived - timeSent
            ttl = ord(struct.unpack('!c', recPacket[8:9])[0].decode())
            return (delay, ttl, byteInDouble)

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return 'Request timed out'

def sendOnePing(mySocket, destAddr, ID):
    # header is type(8) code(8) checksum(16) id(16) sequence(16)
    myChecksum = 0
    # make a dummy header with a 0 checksum
    # struct - interpret strings as packed binary data 
    header = struct.pack('!bbHHh', ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack('!d', time.time())
    # calculate the checksum on the data and the dummy header
    myChecksum = checksum(str(header + data))

    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data 
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str 
    # both LISTS and TUPLES consist of a number of objects 
    # which can be referenced by their position number within the object

def doOnePing(destAddr, timeout):
    icmp = getprotobyname('icmp')
    # SOCK_RAW is a powerful socket type, ref: https://sock-raw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xffff # return the current process i
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay 

def ping(host, timeout=1):
    # timeout=1 means: if one second goes by without a reply from the server 
    # the client assumes that either the client's ping or the server's pong is lost 
    dest = gethostbyname(host)
    print('Pinging ' + dest + ' using Python')
    print('')
    # send ping requests to a server separated by approximately one second 
    loss = 0
    for i in range(4):
        pass

ping('baidu.com')