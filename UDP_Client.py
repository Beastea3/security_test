from socket import *

target_ip = "127.0.0.1"
target_port = 9998

client = socket(AF_INET, SOCK_DGRAM)
#client.bind((target_ip, target_port))

while True:
    data = raw_input('>> ')
    if not data:
        break
    client.sendto(data, (target_ip, target_port))
    response = client.recvfrom(2046)
    print response
    break


client.close()