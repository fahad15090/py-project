#Host-to-ip simplest
import socket 
hostname = str(input ())
ip = socket.gethostbyname(hostname)
print('Hostname: ', hostname, '\n' 'IP: ', ip )
