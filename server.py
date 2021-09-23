import socket
import threading

from parseparams import parseParams
from sharedmem import sharedMem
from jsontools import loadJSON
from userauth import isUserAuthorized
from handlebots import getBots

[HOST_IP, PORT, BUFFER_SIZE] = parseParams('params.txt')

usercreds = sharedMem(loadJSON('user_credentials.json'))
bots = getBots()

server = socket.socket()
server.bind((HOST_IP, PORT))
server.listen(5)
print('server running on ' + HOST_IP + ':' + str(PORT))
print('waiting for clients...')

def serveClient(client, address, userinit):
    [username, userpass] = userinit.split('<SEP>')
    isauth = "SUCCESS" if isUserAuthorized(usercreds, username, userpass) else "FAIL"
    client.send(str.encode(isauth))
    if(isauth == "SUCCESS"):
        print('client connected ' + address[0] + ':' + str(address[1]))
        while True:
            command = client.recv(BUFFER_SIZE).decode('utf-8')
            if(command == "exit"):
                break
            else:
                spl = command.find(' ')
                if(spl >= 0):
                    handle = command[:spl].strip()
                    value = command[spl:].strip()
                    if(handle in bots):
                        client.send(str.encode(bots[handle](value)))
                    else:
                        client.send(str.encode("Invalid bot"))
                else:
                    client.send(str.encode("Invalid command"))
        print('client disconnected ' + address[0] + ':' + str(address[1]))
    client.close()

while True:
    (client, address) = server.accept()
    userinit = client.recv(BUFFER_SIZE).decode('utf-8')
    if(userinit.lower() == "kill"):
        client.close()
        print('killing server')
        break
    else:
        client_thread = threading.Thread(target = serveClient, args = (client, address, userinit, ))
        client_thread.start()

