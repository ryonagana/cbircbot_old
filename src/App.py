'''
Created on 28/10/2011

@author: Nicholas


'''

import Config
import IRCProtocol
import Module


class App(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        self.conf = Config.Config("config.cfg")
        self.data = Config.ConfigData()
        
        
        self.data.nick =  self.conf.Get("config", "nick")
        self.data.email= self.conf.Get("config", "email" )
        self.data.realname = self.conf.Get("config", "realname")
        self.data.channel = self.conf.Get("config", "channel")
        self.data.server = self.conf.Get("config", "server")
        self.data.port   = self.conf.GetInt("config", "port")
        self.data.needidentify = self.conf.GetBool("config", "needIdentify")
        self.data.ident = self.conf.Get("config", "ident")
        
        
        if( self.data.needidentify == True and  self.data.needidentify != None  ):
            self.data.userpass = self.conf.Get("config", "password")
        else:
            self.data.userpass = self.conf.Get("config", "password")
        if ( self.data.userpass != None):
            print "[Warning:] Config.cfg: please clear line of your password if needIdentify is False"
        
        
        self.conf.AssignClientData(self.data)
    
    
        self.c = IRCProtocol.Client(self.data.server, self.data.port, self.data.nick, self.data.realname, self.data.email, self.data.ident)
    
        self.c.AssignConfig(self.conf)
    
        self.mod = Module.Module("config.cfg", "modules")
    
        self.mod.ReadAllModules()
    
    #mod.ReadList(c)
    

    
        self.c.Connect()
    
        self.c.CreateIdentity()
        self.c.JoinChannel(self.data.channel)
    
    
    
        self.botmessage = ""
    
        self.c.startUserInputThread(self.data)
        self.c.StartTimeoutThread(30)
        
    def Start(self):
        while True:
            server = []
        
            self.botmessage =  self.c.SocketObject().recv(1024)
            self.c.CheckPing(self.botmessage)
            server.append(self.botmessage)
        
            print server[0]
            self.botmessage = None
            del server
        
        
        