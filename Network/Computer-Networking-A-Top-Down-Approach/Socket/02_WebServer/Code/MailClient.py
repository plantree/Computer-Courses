from base64 import encode
from socket import *
import base64

msg = 'I love computer networks'
endmsg = '\r\n.\r\n'

# choose a mail server, ref: https://github.com/moranzcw/Computer-Networking-A-Top-Down-Approach-NOTES/blob/master/SocketProgrammingAssignment/%E4%BD%9C%E4%B8%9A3-%E9%82%AE%E4%BB%B6%E5%AE%A2%E6%88%B7%E7%AB%AF/TSL%E5%92%8C%E5%8F%91%E9%80%81%E6%B7%B7%E5%90%88%E7%B1%BB%E5%9E%8Bemail.py
mailserver = 'smtp.qq.com'
fromaddr = '**@qq.com'
toaddr = '**@qq.com'
# ref: https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
user = '**@qq.com'
passw = '**'
user = base64.b64encode(user.encode()).decode()
passw = base64.b64encode(passw.encode()).decode()
serverPort = 25
serverPortTLS = 587

# create socket called clientSockt and establish a TCP connection with mailserver 
clientSockt = socket(AF_INET, SOCK_STREAM)
clientSockt.connect((mailserver, serverPort))

recv = clientSockt.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server')

# send HELO command and print server response 
heloCommand = 'HELO Alice\r\n'
clientSockt.send(heloCommand.encode())
recv1 = clientSockt.recv(1024).decode()
print('recv1:', recv1)
if recv1[:3] != '250':
    print('250 reply not received from server')

# using TLS
'''
tlsCommand = 'STARTTLS\r\n'
clientSockt.send(tlsCommand.encode())
recv2 = clientSockt.recv(1024).decode()
print('recv2:', recv2)
'''

# Auth
authCommand = 'AUTH LOGIN\r\n'
clientSockt.send(authCommand.encode())
recv3 = clientSockt.recv(1024).decode()
print('recv3:', recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

userCommand = '{0}\r\n'.format(user)
clientSockt.send(userCommand.encode())
recv4 = clientSockt.recv(1024).decode()
print('recv4:', recv4)
if (recv4[:3] != '334'):
	print('334 reply not received from server')

passCommand = '{0}\r\n'.format(passw)
clientSockt.send(passCommand.encode())
recv5 = clientSockt.recv(1024).decode()
print('recv5:', recv5)
if (recv5[:3] != '235'):
	print('235 reply not received from server')

# send MAIL FROM command and print server response
fromCommand = 'MAIL FROM:<{0}>\r\n'.format(fromaddr)
clientSockt.send(fromCommand.encode())
recv6 = clientSockt.recv(1024).decode()
print('recv6:', recv6)
if (recv6[:3] != '250'):
	print('250 reply not received from server')

# send RCPT TO command and print server response
toCommand = 'RCPT TO:<{0}>\r\n'.format(toaddr)
clientSockt.send(toCommand.encode())
recv7 = clientSockt.recv(1024).decode()
print('recv7:', recv7)
if (recv7[:3] != '250'):
	print('250 reply not received from server')

# send DATA command and print server response
dataCommand = 'DATA\r\n'
clientSockt.send(dataCommand.encode())
recv8 = clientSockt.recv(1024).decode()
print('recv8:', recv8)
if (recv8[:3] != '354'):
	print('354 reply not received from server')

# send message data 
sendText = 'From:%s\r\nTo:%s\r\nSubject:hello,you!\r\nContent-Type:text/plain\n\r\n' % (fromaddr, toaddr) + msg + endmsg
print(sendText)
clientSockt.send(sendText.encode())
recv9 = clientSockt.recv(1024).decode()
print('recv9:', recv9)

# send QUIT command and get server response
quitMsg = 'QUIT\r\n'
clientSockt.send(quitMsg.encode())
recv10 = clientSockt.recv(1024).decode()
print('recv10:', recv10)

clientSockt.close()