from socket import *

class Mail():

    msg = '\r\nI love computer networks! \r\n'
    endmsg = '\r\n.\r\n'

    mailServer = 'gaia.ecs.csus.edu' 
    
    def connection(self):
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.mailServer, 25))
        recv = self.clientSocket.recv(1024)
        print(recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')

        helloCommand = 'Helo Alice\r\n'
        self.clientSocket.send(helloCommand.encode())
        recv1 = self.clientSocket.recv(1024).decode()
        print(recv1)
        if recv1[:3] != '250':
            print('250 reply not received from server.')


        mailCommand = 'Mail from: <vibhoresagar@ecs.csus.edu>\r\n'
        self.clientSocket.send(mailCommand.encode())
        recv2= self.clientSocket.recv(1024).decode()
        print(recv2)
        if recv2[:3] != '250':
            print('250 reply not received from server')


        rcptCommand = 'RCPT to: <vibhoresagar@csus.edu>\r\n'
        self.clientSocket.send(rcptCommand.encode())
        recv3 = self.clientSocket.recv(1024).decode()
        print(recv3)
        if recv3[:3] != '250':
            print('250 reply not received from server.')


        dataCommand = 'Data \r\n'
        self.clientSocket.send(dataCommand.encode())
        recv4 =self. clientSocket.recv(1024).decode()
        print(recv4)
        if recv4[:3] != '354':
            print('354 reply not received from server.')

        

    def sendMessage(self):

        self.clientSocket.send(self.msg.encode())

        self.clientSocket.send(self.endmsg.encode())
        recv5 = self.clientSocket.recv(1024).decode()
        print(recv5)

        quitCommand= 'Quit \r\n'
        self.clientSocket.send(quitCommand.encode())
        recv5 = self.clientSocket.recv(1024).decode()
        print(recv5)
        if recv5[:3] != '221':
            print('221 reply not received from server.')
    


if __name__ == "__main__":
    m = Mail()
    m.connection()
    m.sendMessage()
    