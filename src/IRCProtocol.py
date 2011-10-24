from socket import socket, AF_INET, SOCK_STREAM, SHUT_WR
import sys
#connector deal with sockes
class Connector:
    def __init__(self, server,port):
        self.socket  = socket(AF_INET, SOCK_STREAM)
        self.server = server
        self.port = port
        
        self.isConnected = False
        
        
    def SocketObject(self):
        return self.socket
    
    def Connect(self):
        self.socket.connect((self.server,self.port))
        
        testconn =  self.socket.recv(4096)
        
        if testconn != None:
            self.isConnected = True
        else:
            print "Cannot Connect on " +  self.server + ":" + self.port
            exit(0)
            
    def Close(self):
        self.socket.close()
        self.socket.shutdown(SHUT_WR)
        

#CLIENT CLASS

class Client(Connector):
    def __init__(self, server, port, nickname, realname, email, ident ):
        
        self.nick = nickname
        self.realname = realname
        self.email = email
        self.ident = ident
        #self.server = server
        #self.port = port
        Connector.__init__(self, server, port)
        
        #super(Client, self).__init__(server,port)
        
    
    def SendMessage(self, message):
        
        if( self.isConnected):
            text = message + '\r\n'
            self.socket.send(text)
            
    def CheckPing(self, message):
        
        if self.isConnected:
            if message.find("PING") != -1:
                self.SendMessage("PONG " +  message.split()[1])
                print "PONG'd  {0} ".format(message.split()[1])
        else:
            sys.stderr << "Ping not send"
                
                
    def CreateIdentity(self):
        
        if( self.isConnected):
           
            self.SendMessage('NICK ' + self.nick )
            
            user = 'USER {0} {1} :bla  {2}'.format(self.ident, self.server, self.realname)   
            
            
            self.SendMessage(user)
            
        else:
            sys.stderr << "Cannot create a new identity f you are disconnectd"
    
    def JoinChannel(self, channel):
        
        if self.isConnected:
            self.SendMessage("JOIN " +  channel)
            
            
    def Talk(self, message, channel,  user = None):
        
        tmpmsg = ""
        
        if user == None:
            tmpmsg  = "PRIVMSG {0} :{1} ".format(channel, message)
        else:
            tmpmsg  = "PRIVMSG {0} :{1} ".format(user, message)
            
            
            if (self.isConnected):
                self.SendMessage(tmpmsg)
                
                
    def TalkOnChannel(self, message, channel):
            if( self.isConnected):
                tmp = ""
                
                #tmp.format("PRIVMSG %s :%s", channel, message )
                tmp  = "PRIVMSG {0} :{1} ".format(channel, message)
                self.SendMessage(tmp)
                
    def ChangeNick(self, oldname, newname):        
        temp = ":{0} NICK {1}".format(oldname,newname)
        self.SendMessage(temp)
        
    
                
                
        
       
                    
    
    
        
        
        