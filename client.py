import socket
import sys

from parseparams import parseParams

[HOST_IP, PORT, BUFFER_SIZE] = parseParams()

if(len(sys.argv) == 2):
    userinit = sys.argv[1]
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
        print("AUTH:", isauth)
        if(isauth):
            while True:
                command = input().lower()
                server.send(str.encode(command))
                if(command == "exit"):
                    break
        server.close()
    print('connection closed')
except socket.error as e:
    print(str(e))