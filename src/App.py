'''
Created on 28/10/2011

@author: Nicholas


'''

import Config
import IRCProtocol
import Modules
import TwitterAPI
import sys,time, re

class App(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        self.conf = Config.Config("config.cfg")
        self.data = Config.ConfigData()
        self.modulelist = None
        
        
        '''
        pega configuracoes do arquivo config.cfg e atribui na classe de configuracao
        '''
        
        self.data.nick =  self.conf.Get("config", "nick")
        self.data.email= self.conf.Get("config", "email" )
        self.data.realname = self.conf.Get("config", "realname")
        self.data.channel = self.conf.Get("config", "channel")
        self.data.server = self.conf.Get("config", "server")
        self.data.port   = self.conf.GetInt("config", "port")
        self.data.needidentify = self.conf.GetBool("config", "needIdentify")
        self.data.ident = self.conf.Get("config", "ident")
        
        #twitter integration
        self.data.consumer_key = ""
        self.data.consumer_secret = ""
        self.data.access_key = ""
        self.data.access_secret = ""
        
        
        self.parsedata = []
        self.rawdata = []
        
        
        
        
        ''' checa se a pessa fez identify no nick se caso esta registrado  '''
        
        if( self.data.needidentify == True and  self.data.needidentify != None  ):
            self.data.userpass = self.conf.Get("config", "password")
        else:
            self.data.userpass = self.conf.Get("config", "password")
        if ( self.data.userpass != ""):
            print "[Warning:] Config.cfg: please clear line of your password if needIdentify is False"
        
        

        
        ''' 
            Ativando Twitter
        '''
        self.data.consumer_key = self.conf.Get("twitter", "consumer_key")
        self.data.consumer_secret = self.conf.Get("twitter", "consumer_secret")
        self.data.access_key = self.conf.Get("twitter", "access_key")
        self.data.access_secret = self.conf.Get("twitter", "access_secret")
        self.data.user =   self.conf.Get("twitter", "user")
        
        self.auth = TwitterAPI.TwitterAuth(self.data.consumer_key, self.data.consumer_secret, self.data.access_key, self.data.access_secret)
        
        if(self.data.consumer_key == ""  or  self.data.consumer_secret == "" or self.data.access_key == ""  or self.data.access_secret == ""):
            #sys.stderr << "Twitter API Not Active:  REASON: need the correct consumer keys and access_tokens"
            print "Twitter API not Activated"
        else:
            self.twitter = TwitterAPI.TwitterAPI(self.data.user, self.auth)
            
            
        
            
        
        #self.modules.executeModules()
        
        
        ''' passa as informacoes da config.cfg pra outras classes'''
        self.conf.AssignClientData(self.data)
    
        ''' inicia Conexao ( inicia socket conecta no endereco cru (sem suporte a proxy no momento) '''
        self.irclient = IRCProtocol.Client(self.data.server, self.data.port, self.data.nick, self.data.realname, self.data.email, self.data.ident, self.data )
        
   
 
        
        self.irclient.Connect() # conecta 
        self.irclient.CreateIdentity() #cria uma nova identity no IRC
        self.irclient.JoinChannel(self.data.channel) #entra no canal desejado
    
        ''' Inicia com cuidado 2 threads:
            o primeiro adiciona o suporte ao admin do bot digitar comandos diretamente no console
            o segundo checa conexao time out do servidor e espera 30 segundos para cada checagem
             '''
        
        
        ''' carrega a lista de modulos existente  '''
        self.InitModules()
  
        
        
        try:
            self.irclient.startUserInputThread(self.data)
            self.irclient.StartTimeoutThread(30)
        except KeyboardInterrupt:
            sys.exit()
        
       
        
    def InitModules(self):
            self.data.modules = self.conf.Get("modules", "modules")
            self.modules = Modules.Modules(self.data)
            self.modules.RunModules(self.irclient)    
    
        
    def PrintMessage(self, message ):
        print "Server: " + message;
        
    def ParsedMessage(self, message):
        
        tmp = message.split(":")
        self.parsedata = tmp;
    

    def FilterMessage(self, msg):
        
        try:
        
            cut = msg.split(' ')[3:]
                
            
            
            self.parsedata.append(cut)
        except Exception:
            print "Erro ao tentar dar Parse"


    def RunCommands(self): 
        
        for instance in self.modules.moduleinstances:
            #if(self.parsedata[0]  == self.data.nick and  instance.args.cmdname == self.parsedata[1]):
            
            masksender = re.compile(":(.*)!", re.IGNORECASE)
            maskchannel = re.compile("(#.\w+)", re.IGNORECASE)
            
            searchsender = masksender.search(self.rawdata[0])
            searchchannel = maskchannel.search(self.rawdata[0])

            
            instance.args.sender = masksender.findall(self.rawdata[0])
            instance.args.channelsent = maskchannel.findall(self.rawdata[0])
            instance.args.args =  self.parsedata
            instance.Execute(instance.args.sender, instance.args.channelsent)
            
                
                 
        
       
    def Start(self):
        while True:
            
            try:
                
                server = self.irclient.socket.recv(1024); #recebe dados do servidor e atribui a variavel server
                self.FilterMessage(server)
                self.rawdata.append(server)
                self.irclient.CheckPing(server) #  checa ping se o servidor envia pedido de ping eo cliente responde com PONG
                self.PrintMessage(server) #imprime mensagem
                #self.ParsedMessage(server) # separa mensagem
                for msg in self.parsedata:
                    self.RunCommands()
                #print self.parsedata   #print na mensagem
                time.sleep(0.5)
                
                if( len(self.parsedata) > 0):
                    self.parsedata.pop()
                if( len( self.parsedata) > 0 ):
                    self.rawdata.pop()
                
              
            except KeyboardInterrupt:
                self.irclient.stopUserInputThread()
                sys.exit(0)
        
        
        