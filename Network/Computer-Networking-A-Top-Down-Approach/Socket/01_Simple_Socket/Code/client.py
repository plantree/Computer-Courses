import socket 

client_name = 'pengyuan'
server_addr = '127.0.0.1'
server_port = 8000

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect 
s.connect((server_addr, server_port))
sum = 0
while True:
    # get input
    num = input('input(between 1-100): ')
    s.send(('{0} {1}'.format(client_name, num)).encode())
    data = s.recv(1024)
    if not data:
        break 
    text = data.decode()
    server_name, num = text.split(' ')
    try:
        num = int(num)
    except Exception as e:
        break
    if num < 1 or num > 100:
        break 
    sum += num
    print('Get from server({0}): {1}, accumulate: {2}'.format(server_name, num, sum))    
s.close()

