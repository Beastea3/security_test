# import module
from socket import *

target_ip = "127.0.0.1"
target_port = 9999
# socket(socket_family, socket_type, protocol=0(default))
client = socket(AF_INET, SOCK_STREAM)

client.connect((target_ip, target_port))

client.send("GET / HTTP/1.1\r\nHost:localhost\r\n\r\n")

response = client.recv(4096)

print response
