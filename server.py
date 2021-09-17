import socket
import threading

from sharedmem import sharedMem
from jsontools import loadJSON
from userauth import isUserAuthorized

host_ip = '192.168.29.156'
port = 2004
BUFFER_SIZE = 4096

usercreds = sharedMem(loadJSON('user_credentials.json'))

server = socket.socket()
server.bind((host_ip, port))
server.listen(5)
print('Server waiting for clients')

while True:
    (client, address) = server.accept()
    userinit = client.recv(BUFFER_SIZE).decode('utf-8')
    if(userinit.lower() == "kill"):
        client.close()
        break
    else:
        [username, userpass] = userinit.split('<SEP>')
        print(username, userpass)
        isauth = isUserAuthorized(usercreds, username, userpass)
        client.send(str.encode("SUCCESS" if isauth else "FAIL"))
        if(isauth):
            while True:
                command = client.recv(BUFFER_SIZE).decode('utf-8')
                print(command)
                if(command == "exit"):
                    break
        client.close()
