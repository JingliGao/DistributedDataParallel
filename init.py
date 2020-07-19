import os
"""
import socket
import fcntl
import struct


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode("utf-8"))
    )[20:24])

with open('IP','w') as wf:
    wf.write(get_ip_address('eth0'))
f = open('IP', 'r')
print(f.read())
"""



os.environ['MASTER_ADDR']=input("Input MASTER_ADDR:")
print(os.environ['MASTER_ADDR'])
os.environ['MASTER_PORT'] = input("Input MASTER_PORT:")
print(os.environ['MASTER_PORT'])



