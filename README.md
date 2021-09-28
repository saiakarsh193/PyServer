# PyServer-Shell  
## Sai Akarsh (17-09-21)  

### Description  
Simple remote terminal hosted on a socket based server.  
The shell allows a few basic commands to communicate with the server.  
Please read [the notes](#note) before running the program.  

### Commands  
- `upload` to upload a file to the server
- `download` to download a file from the server
- `list` to list the files in the server
- `remove` to remove a file from the server
- `exit` to exit the server

### Running the Server  
To start the server, run the command  
`python server.py`  

### Running the Client  
To start the client, run the command  
`python client.py <username> <password>`  

You can find the user credentials in the `user_credentials.json` file. To add a new account, you can change that file on server side.  
This can be done by adding a new entry in the format `["<username>", "<password>"]`.  

### Note  
- Change the `HOST_IP` in the `params.txt` to the local ip address of the system on which you are running `server.py`.  
  You can also change the other parameters if necessary, but make sure that **both the server and client are using the same parameters**.  
- The program works only over LAN (Local Area Network). The internet is a dangerous place. Making the server visible to everyone is as good as inviting unwanted guests to your doorstep. To make this program safe to use, it is better to use it via LAN. Since this is just an experimental program, try not to modify this for over the LAN support.  
- To use client program without the support files, you can hardcode the parameters directly in `client.py`. This will allow you to run `client.py` on its own.  

  Modify (in `client.py`)  

  ```python
  from parseparams import parseParams
  [HOST_IP, PORT, BUFFER_SIZE] = parseParams('params.txt')
  ```  
  to  
  
  ```python
  [HOST_IP, PORT, BUFFER_SIZE] = [<HOST_IP>, <PORT>, <BUFFER_SIZE>]
  ```  
  Replace `<HOST_IP>` with the ip of server side system, for example `192.168.29.145`  
  Replace `<PORT>` with the port on which the server is running on, for example `2004`  
  Replace `<BUFFER_SIZE>` with your choice of buffer size. **It is required to have the same buffer size on server side too. Otherwise the program wont work**, recommended value is `4096`  
- To stop the server, we need to activate the kill client, which will kill the server as soon as no client is connected anymore.  
  To activate kill client, run the client using  
  `python client.py kill`
