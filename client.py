import socket
import sys

host_ip = '192.168.29.156'
port = 2004
BUFFER_SIZE = 4096

if(len(sys.argv) == 2):
    userinit = sys.argv[1]
elif(len(sys.argv) == 3):
    userinit = sys.argv[1] + "<SEP>" + sys.argv[2]
else:
    print("Invalid arguments")
    sys.exit(0)

server = socket.socket()

try:
    print('Waiting for server to respond')
    server.connect((host_ip, port))
    server.send(str.encode(userinit))
    if(userinit.lower() == "kill"):
        server.close()
    else:
        isauth = server.recv(BUFFER_SIZE).decode('utf-8')
        print(isauth)
        if(isauth):
            while True:
                command = input().lower()
                server.send(str.encode(command))
                if(command == "exit"):
                    break
        server.close()
except socket.error as e:
    print(str(e))