'''
Created on 28/10/2011

@author: Nicholas


'''

import Config
import IRCProtocol
import Modules
import sys

class App(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        self.conf = Config.Config("config.cfg")
        self.data = Config.ConfigData()
        self.modulelist = None
        
        
        self.data.nick =  self.conf.Get("config", "nick")
        self.data.email= self.conf.Get("config", "email" )
        self.data.realname = self.conf.Get("config", "realname")
        self.data.channel = self.conf.Get("config", "channel")
        self.data.server = self.conf.Get("config", "server")
        self.data.port   = self.conf.GetInt("config", "port")
        self.data.needidentify = self.conf.GetBool("config", "needIdentify")
        self.data.ident = self.conf.Get("config", "ident")
        
        self.parsedata = []
        
        
        if( self.data.needidentify == True and  self.data.needidentify != None  ):
            self.data.userpass = self.conf.Get("config", "password")
        else:
            self.data.userpass = self.conf.Get("config", "password")
        if ( self.data.userpass != None):
            print "[Warning:] Config.cfg: please clear line of your password if needIdentify is False"
        
        
        
        self.data.modules = self.conf.Get("modules", "modules")
        
        self.modules = Modules.Modules(self.data)
        self.conf.AssignClientData(self.data)
    
    
        self.irclient = IRCProtocol.Client(self.data.server, self.data.port, self.data.nick, self.data.realname, self.data.email, self.data.ident, self.data )
        self.irclient.Connect()
        self.irclient.CreateIdentity()
        self.irclient.JoinChannel(self.data.channel)
    
    
    
        self.irclient.startUserInputThread(self.data)
        self.irclient.StartTimeoutThread(30)
        
       
        
        

        
    def PrintMessage(self, message ):
        print "Server: " + message;
        
    def ParsedMessage(self, message):
        
        tmp = message.split(":")
        self.parsedata = tmp;
    
        
        
    def Start(self):
        while True:
            
            try:
                
                server = self.irclient.socket.recv(1024);
                self.irclient.CheckPing(server)
                self.PrintMessage(server)
                self.ParsedMessage(server)
                
                print self.parsedata
                
                del server
                
              
            except KeyboardInterrupt:
                sys.exit(0)
        
        
        