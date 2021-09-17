import socket
import threading

from parseparams import parseParams
from sharedmem import sharedMem
from jsontools import loadJSON
from userauth import isUserAuthorized

[HOST_IP, PORT, BUFFER_SIZE] = parseParams()

usercreds = sharedMem(loadJSON('user_credentials.json'))

server = socket.socket()
server.bind((HOST_IP, PORT))
server.listen(5)
print('server running on ' + HOST_IP + ':' + str(PORT))
print('waiting for clients...')

while True:
    (client, address) = server.accept()
    userinit = client.recv(BUFFER_SIZE).decode('utf-8')
    if(userinit.lower() == "kill"):
        client.close()
        print('killing server')
        break
    else:
        [username, userpass] = userinit.split('<SEP>')
        print(username, userpass)
        isauth = isUserAuthorized(usercreds, username, userpass)
        client.send(str.encode("SUCCESS" if isauth else "FAIL"))
        if(isauth):
            print('client connected ' + address[0] + ':' + str(address[1]))
            while True:
                command = client.recv(BUFFER_SIZE).decode('utf-8')
                print(command)
                if(command == "exit"):
                    break
            print('client disconnected ' + address[0] + ':' + str(address[1]))
        client.close()
