from socket import  *

bind_ip = "127.0.0.1"
bind_port = 9998

server = socket(AF_INET, SOCK_DGRAM)
server.bind((bind_ip, bind_port))

while True:
    print 'Waiting for message'
    data, addr = server.recvfrom(2046)
    server.sendto(data, addr)
    print 'received from and returned to:', addr



server.close()