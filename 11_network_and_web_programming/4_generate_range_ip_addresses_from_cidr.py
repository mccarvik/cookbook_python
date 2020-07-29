# Can generate range of all ip addresses over a network address
import ipaddress, pdb
net = ipaddress.ip_network('123.45.67.64')
print(net)

for a in net:
    print(a)
net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
print(net6)

for a in net6:
    print(a)

print(net.num_addresses)
print(net[0])
# print(net[1])
# print(net[-1])
# print(net[-2])
a = ipaddress.ip_address('123.45.67.69')
print(a in net)
b = ipaddress.ip_address('123.45.67.123')
print(b in net)
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)

a = ipaddress.ip_address('127.0.0.1')
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
# s.connect((a, 8080)) # will cause error, cant convert ipv4address, needs to be str
s.connect((str(a), 8080))
