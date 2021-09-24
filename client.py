import socket
import sys

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
                if(command == "exit"):
                    server.send(str.encode(command))
                    break
                else:
                    spl = command.find(' ')
                    if(spl >= 0):
                        handle = command[:spl].strip()
                        value = command[spl:].strip()
                    else:
                        handle = command
                        value = ""
                    server.send(str.encode(handle + "<SEP>" + value))
                    response = server.recv(BUFFER_SIZE).decode('utf-8')
                    print(response)
            print("pyserver_shell stopped")
        else:
            print("Invalid user details")
        server.close()
    print('connection closed')
except socket.error as e:
    print(str(e))