import socket
import sys
import os
import math

from parseparams import parseParams

[HOST_IP, PORT, BUFFER_SIZE] = parseParams('params.txt')

if(len(sys.argv) == 2):
    if(sys.argv[1].lower() == "kill"):
        userinit = sys.argv[1]
    else:
        userinit = sys.argv[1] + "<SEP>" + "0"
elif(len(sys.argv) == 3):
    userinit = sys.argv[1] + "<SEP>" + sys.argv[2]
else:
    print("invalid arguments")
    sys.exit(0)

server = socket.socket()

try:
    print('waiting for server to respond')
    server.connect((HOST_IP, PORT))
    print('connected to server on ' + HOST_IP + ':' + str(PORT))
    server.send(str.encode(userinit))
    if(userinit.lower() == "kill"):
        server.close()
        print('sending kill server command')
    else:
        isauth = server.recv(BUFFER_SIZE).decode('utf-8')
        if(isauth == "SUCCESS"):
            print("pyserver_shell running...")
            while True:
                command = input(">> ").lower().strip()
                if(len(command) == 0):
                    continue
                spl = command.find(' ')
                if(spl >= 0):
                    handle = command[:spl].strip()
                    value = command[spl:].strip()
                else:
                    handle = command
                    value = ""
                if(handle == "upload" or handle == "upf"):
                    if(os.path.isfile(value)):
                        fvalue = value
                        value = os.path.basename(fvalue)
                    else:
                        print("Invalid file")
                        continue
                server.send(str.encode(handle + "<SEP>" + value))
                if(handle == "exit"):
                    break
                elif(handle == "upload" or handle == "upf"):
                    filesize = os.path.getsize(fvalue)
                    segs = math.ceil(filesize / BUFFER_SIZE)
                    server.send(str.encode(str(segs)))
                    server.recv(BUFFER_SIZE).decode('utf-8')
                    with open(fvalue, 'r') as f:
                        for _ in range(segs):
                            data = f.read(BUFFER_SIZE)
                            if(data == ""):
                                data = "<NULL>"
                            server.send(str.encode(data))
                elif(handle == "download" or handle == "dnf"):
                    segs = server.recv(BUFFER_SIZE).decode('utf-8')
                    segs = int(segs)
                    server.send(str.encode("ACK"))
                    if(segs >= 0):
                        value = os.path.basename(value)
                        with open(value, 'w') as f:
                            for _ in range(segs):
                                data = server.recv(BUFFER_SIZE).decode('utf-8')
                                if(data != "<NULL>"):
                                    f.write(data)
                response = server.recv(BUFFER_SIZE).decode('utf-8')
                print(response)
            print("pyserver_shell stopped")
        else:
            print("Invalid user details")
        server.close()
    print('connection closed')
except socket.error as e:
    print(str(e))