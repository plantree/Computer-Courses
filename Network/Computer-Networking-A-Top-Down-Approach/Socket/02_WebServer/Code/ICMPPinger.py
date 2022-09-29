from datetime import timedelta
from socket import *
import os 
import struct 
import time 
import select 

ICMP_ECHO_REQUEST = 8

def checksum(str):
    csum = 0
    countTo = (len(str) / 2) * 2
    count = 0
    while count < countTo:
        thisVal = str[count + 1] * 256 + str[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2
    if countTo < len(str):
        csum = csum + str[len(str) - 1].decode()
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
            return None

        timeReveived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # fetch the ICMP header from the IP packet 
        # IP header size is 20
        header = recPacket[20:28]
        type, code, checksum, packetID, seq = struct.unpack('!bbHHh', header)
        if type == 0 and packetID == ID:    # type should be 0
            byteInDouble = struct.calcsize('!d')
            timeSent = struct.unpack('!d', recPacket[28:28 + byteInDouble])[0]
            delay = timeReveived - timeSent
            ttl = ord(struct.unpack('!c', recPacket[8:9])[0].decode())
            return (delay, ttl, byteInDouble)

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return None

def sendOnePing(mySocket, destAddr, ID):
    # header is type(8) code(8) checksum(16) id(16) sequence(16)
    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("!d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object

def doOnePing(destAddr, timeout):
    icmp = getprotobyname('icmp')
    # SOCK_RAW is a powerful socket type, ref: https://sock-raw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xffff # return the current process i
    sendOnePing(mySocket, destAddr, myID)
    ret = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return ret 

def ping(host, timeout=2):
    # timeout=1 means: if one second goes by without a reply from the server 
    # the client assumes that either the client's ping or the server's pong is lost 
    dest = gethostbyname(host)
    print('Pinging ' + dest + ' using Python')
    print('')
    # send ping requests to a server separated by approximately one second 
    loss = 0
    for i in range(4):
        result = doOnePing(dest, timeout)
        if not result:
            print('Request time out')
            loss += 1
        else:
            delay = int(result[0] * 1000)
            ttl = result[1]
            bytes = result[2]
            print('Received from ' + dest + ": bytes(s)" + str(bytes) + " delay = " + str(delay) + "ms TTL = " + str(ttl))
        time.sleep(1)
    print('Packet: send=4' + " received = " + str(4 - loss))

ping('baidu.com')