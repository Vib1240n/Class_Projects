import threading
import _thread
from _thread import *
from socket import *
import datetime

lock = threading.Lock()


class server_thread(threading.Thread):

    def __init__(self, connectionSocket, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.address = address

    def thread(self):
        while True:
            message = connectionSocket.recv(1024)
            if not message:
                print("No message")
                lock.release()
                break

            filename = message.split()[1]                  
            file = open(filename[1:])                         
            outputdata = file.read()    
            connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8')) 
            try:         
                for i in range(0, len(outputdata)):     
                    connectionSocket.send(bytes((outputdata[i]),'UTF-8')) 
                connectionSocket.close() 
            except IOError:  
                    connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8', 'UTF-8'))
                    connectionSocket.sendall(bytes('HTTP/1.1 404 Not Found\r\n\r\n','UTF-8', 'UTF-8'))
                    connectionSocket.close()
        connectionSocket.close()




if __name__ == "__main__":
    severName = 'hostname'
    serverPort = 7070
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('192.168.0.23', serverPort)) 
    print("Socket Binded")
    serverSocket.listen(1)
    threads = []
    while True:
        print(' Ready to serve... ')
        connectionSocket, addr = serverSocket.accept()
        newThread = server_thread(connectionSocket, addr)
        newThread.start()
        threads.append(newThread)
        serverSocket.close()
        for i in threads:
            i.join()
