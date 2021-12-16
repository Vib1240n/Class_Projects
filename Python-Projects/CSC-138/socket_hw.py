import ipaddress
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
severName = 'hostname'
serverPort = 7070
serverSocket.bind(('192.168.0.23', serverPort))
serverSocket.listen(1)
print("The server is ready to listen")
while True: 
    #Establish the connection 
    print(' Ready to serve... ')
    connectionSocket, addr = serverSocket.accept()      
    try: 
        message = connectionSocket.recv(1024)             
        filename = message.split()[1]                  
        file = open(filename[1:])                         
        outputdata = file.read()     
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))          
        for i in range(0, len(outputdata)):     
             connectionSocket.send(bytes((outputdata[i]),'UTF-8')) 
        connectionSocket.close() 
    except IOError:  
            connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8', 'UTF-8'))
            connectionSocket.sendall(bytes('HTTP/1.1 404 Not Found\r\n\r\n','UTF-8', 'UTF-8'))
            connectionSocket.close()
    serverSocket.close()
