from socket import *

target_ip = "192.168.0.9"
target_port = 9998

client = socket(AF_INET, SOCK_DGRAM)
client.bind((target_ip, target_port))

while True:
    data = 'gogogogog'
    if not data:
        break
    client.sendto(data, (target_ip, target_port))
    response = client.recvfrom(2046)
    print response
    break


client.close()