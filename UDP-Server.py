from socket import  *

bind_ip = "127.0.0.1"
bind_port = 9998

server = socket(AF_INET, SOCK_DGRAM)
server.bind((bind_ip, bind_port))

while True:
    print 'Waiting for message'
    print 'received from and returned to:'
    data, addr = server.recvfrom(2046)
    print 'received from and returned to:'
    server.sendto(data, addr)
    print 'received from and returned to:'



server.close()