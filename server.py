import socket
import threading
import os

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
            [handle, value] = command.split('<SEP>')
            if(handle == "exit"):
                break
            elif(handle == "list" or handle == "ls"):
                liststr = '\n'.join(os.listdir("root"))
                if(len(liststr) == 0):
                    liststr = "No files"
                client.send(str.encode(liststr[:BUFFER_SIZE]))
            elif(handle == "remove" or handle == "rm"):
                value = os.path.basename(value)
                if(os.path.isfile("root/" + value)):
                    os.remove("root/" + value)
                    client.send(str.encode(value + " removed"))
                else:
                    client.send(str.encode("Invalid file"))
            elif(handle == "upload" or handle == "upf"):
                if(not os.path.isdir("root")):
                    os.mkdir("root")
                segs = client.recv(BUFFER_SIZE).decode('utf-8')
                segs = int(segs)
                with open("root/" + value, 'w') as f:
                    for _ in range(segs):
                        data = client.recv(BUFFER_SIZE).decode('utf-8')
                        if(data != "<NULL>"):
                            f.write(data)
                client.send(str.encode("File uploaded"))
            else:
                if(handle in bots):
                    client.send(str.encode(bots[handle](value)))
                else:
                    client.send(str.encode("Invalid bot"))
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
