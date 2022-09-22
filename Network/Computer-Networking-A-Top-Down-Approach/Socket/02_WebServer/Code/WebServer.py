# import socket module
from email import header
from multiprocessing import set_forkserver_preload
from socket import *
import sys
from wsgiref.simple_server import server_version # in order to terminate to the program

server_addr = '127.0.0.1'
listen_port = 6789

serverSocket = socket(AF_INET, SOCK_STREAM)
# prepare a server socket 
serverSocket.bind((server_addr, listen_port))
serverSocket.listen(5)

while True:
    # establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # send one http header line into socket
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        # send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.close()

    except IOError:
        # send response message for file not found
        print('Not found')
        header = 'HTTP/1.1 404 Not Found\n'
        connectionSocket.send(header.encode())
        # close client socket 
        connectionSocket.send('\r\n'.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit() # terminate the program after sending the corresponding data