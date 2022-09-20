from cgi import print_arguments
from concurrent.futures import thread
import socket 
import threading
import random

server_name = 'plantree'
server_addr = '127.0.0.1'
listen_port = 8000

def tcplink(sock, addr):
    sum = 0 
    while True:
        data = sock.recv(1024)
        if not data:
            break 
        text = data.decode()
        client_name, num = text.split(' ')
        try:
            num = int(num)
        except Exception as e:
            break
        if num < 1 or num > 100:
            break 
        sum += num
        print('Get from client({0}): {1}, accumulate: {2}'.format(client_name, num, sum))
        rand_num = random.randint(1, 100)
        sock.send(('{0} {1}'.format(server_name, rand_num)).encode())
    sock.close()
    print('connection from {0} closed'.format(addr))
        

if __name__ == '__main__':
    # create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind
    server_socket.bind((server_addr, listen_port))
    # become a server socket 
    server_socket.listen(5)
    print('listen ', server_addr)

    while True:
        # accept 
        (client_socket, address) = server_socket.accept()
        # create thread 
        t = threading.Thread(target=tcplink, args=(client_socket, address))
        t.start()


