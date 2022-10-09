from socket import *
import sys

listenPort = 8000

# create a server 
tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpServSock.bind(('', listenPort))
tcpServSock.listen(5)

while True:
    # strat receiving data from the client
    print('Ready to serve at port: ' + str(listenPort) + '...')
    tcpCliSock, addr = tcpServSock.accept()
    print('Reveived a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print(message)

    # extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition('/')[2]
    print(filename)

    fileExist = 'false'
    try:
        # check wether the file exist in the cache
        f = open(filename, 'r')
        outputdata = f.readlines()
        fileExist = 'true'
        # Proxy finds a cache hit and generate a response message
        tcpCliSock.send('HTTP/1.0 200 OK\r\n'.encode())
        tcpCliSock.send('Content-Type:text/html\r\n'.encode())
        # send content
        for line in outputdata:
            tcpCliSock.send(line.encode())
        print('Read from cache')
    # error handling for file not found in cache
    except IOError:
        if fileExist == 'false':
            # create a socket on the proxy
            print('Creating socket on proxy')
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace('www.', '', 1)
            print('Host:', hostn)
            try:
                # connect to the socket to port 80
                c.connect((hostn, 80))
                print('Connect to:', hostn)
                # create a temporary file on this socket and ask port 80 for the file requested by the client
                c.send(('GET ' + 'http//' + filename + ' HTTP/1.0\n\n').encode())

                # read the response into buffer
                buff = c.recv(8192)
                print(buff)
                tcpCliSock.sendall(buff)
                # create a new file in the cache for the requested file
                # also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open('./' + filename, 'w')
                tmpFile.writelines(buff.decode().replace('\r\n', '\n'))
                tmpFile.close()
            except Exception as e:
                print('Illegal request, error:', e)
        else:
            # http response message for file not found
            print('File Not Found')
            tcpCliSock.send('HTTP/1.0 404 Not Found\r\n'.encode())
    finally:
        # close the client and the server sockets
        tcpCliSock.close()
tcpServSock.close()