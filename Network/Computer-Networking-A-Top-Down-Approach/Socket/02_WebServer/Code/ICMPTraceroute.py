from socket import *
import os 
import sys
import struct 
import time 
import select 
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 50
TIMEOUT = 2.0
TRIES = 2

# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise. 
# We shall use the same packet that we build in the Ping exercise
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

def build_packet():
    # header is type(8) code(8) checksum(16) id(16) sequence(16)
    myChecksum = 0
    myID = os.getpid() & 0xffff # return the current process i
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    data = struct.pack("!d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, myID, 1)
    packet = header + data
    return packet 

def get_route(hostname):
    destAddr = gethostbyname(hostname)
    print('Traceroute to', destAddr)
    for ttl in range(1, MAX_HOPS):
        timeLeft = TIMEOUT
        for tries in range(TRIES):
            # make a raw socket named mySocket
            icmp = getprotobyname('icmp')
            mySocket = socket(AF_INET, SOCK_RAW, icmp)
            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)
            try:
                d = build_packet()
                mySocket.sendto(d, (destAddr, 1))
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []: # timeout 
                    print('*    *   *   Request timed out(select)')
                else:
                    timeReceived = time.time()
                    recvPacket, addr = mySocket.recvfrom(1024)
                    timeLeft = timeLeft - howLongInSelect
                    if timeLeft <= 0:
                        print('*    *   *   Request timed out(no time left)')
                    else:
                        # fetch the icmp type from the IP packet
                        header = recvPacket[20:28]
                        types, code, checksum, packetId, seq = struct.unpack('!bbHHh', header)
                        if types == 0:
                            bytes = struct.calcsize('!d')
                            timeSent = struct.unpack('!d', recvPacket[28:28 + bytes])[0]
                            print('%d    rtt=%.0f ms    %s' % (ttl, (timeReceived - timeSent) * 1000, addr[0]))
                            return
                        if types == 11 or types == 3:
                            bytes = struct.calcsize('!d')
                            timeSent = struct.unpack('!d', recvPacket[28:28 + bytes])[0]
                            print('%d    rtt=%.0f ms    %s' % (ttl, (timeReceived - startedSelect) * 1000, addr[0]))
                        else:
                            print('error')
                        break
            except timeout:
                continue
            finally:
                mySocket.close()

get_route('baidu.com')