# PyServer-Shell  
## Sai Akarsh (17-09-21)  

### Description  
Simple remote terminal hosted on a socket based server.  
The shell allows a few basic commands to communicate with the server.  

### Commands  
- `exit` to exit the server
- `list` to list the files in the server
- `remove` to remove a file from the server
- `upload` to upload a file to the server

### Running the Server  
To start the server, run the command  
`python server.py`  

### Running the Client  
To start the client, run the command  
`python client.py <username> <password>`  

### Note  
Change the `HOST_IP` in the `params.txt` to the local ip address of the system on which you are running `server.py`.  
The program works only over LAN.  
