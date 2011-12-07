'''
Created on 28/10/2011

@author: Nicholas


'''

import Config
import IRCProtocol
import Modules
import TwitterAPI
import sys,time

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
        
        
        
        
        ''' checa se a pessa fez identify no nick se caso esta registrado  '''
        
        if( self.data.needidentify == True and  self.data.needidentify != None  ):
            self.data.userpass = self.conf.Get("config", "password")
        else:
            self.data.userpass = self.conf.Get("config", "password")
        if ( self.data.userpass != ""):
            print "[Warning:] Config.cfg: please clear line of your password if needIdentify is False"
        
        
        ''' carrega a lista de modulos existente  '''
        self.data.modules = self.conf.Get("modules", "modules")
        self.modules = Modules.Modules(self.data)
        
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
        try:
            self.irclient.startUserInputThread(self.data)
            self.irclient.StartTimeoutThread(30)
        except KeyboardInterrupt:
            sys.exit()
        
       
        
        

        
    def PrintMessage(self, message ):
        print "Server: " + message;
        
    def ParsedMessage(self, message):
        
        tmp = message.split(":")
        self.parsedata = tmp;
    
        

    def Start(self):
        while True:
            
            try:
                
                server = self.irclient.socket.recv(1024); #recebe dados do servidor e atribui a variavel server
                self.irclient.CheckPing(server) #  checa ping se o servidor envia pedido de ping eo cliente responde com PONG
                self.PrintMessage(server) #imprime mensagem
                #self.ParsedMessage(server) # separa mensagem
                
                #print self.parsedata   #print na mensagem
                time.sleep(0.2)
                
              
            except KeyboardInterrupt:
                self.irclient.stopUserInputThread()
                sys.exit(0)
        
        
        