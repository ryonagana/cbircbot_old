'''
Created on 28/10/2011

@author: Nicholas
'''


class CommandType:
    pass



cmdType = CommandType()
cmdType.SERVER = 1
cmdType.CLIENT = 2
cmdType.INVALID = 0


class CommandBase(object):
    def  __init__(self, name, func_class, typecmd, ircprotocol, acceptParams ):
        self.command = name
        self.func = func_class
        self.type = typecmd
        self.irc = ircprotocol
        self.AcceptParams = acceptParams
    
    
    def Execute(self):
        pass
    
    
class CommandList(object):
    def __init__(self, irc):
        self.cmdlist = []
        
        self.cmdlist.append(CommandTeste(irc))
        self.cmdlist.append(CommandXinga(irc))
        self.irc = irc
        
        
        
    def CommandParser(self, command):
        
        '''
        if  command.find("!") !=  -1:
            
            parser = command.split(":")
            print(parser)
            
            sender = parser[1].split("!")
            args = parser[1].split(" ")            
            
        
            for val in self.cmdlist:
                
                if( parser[2].find("!") != -1):
                    if( parser[2].strip() ==  val.command):
                        
                       
                        val.args = args
                        val.sender = sender
                        val.Execute()
                    
                        #val.Execute()
                    
'''
        
        
            
        cmdparse = command.split(":") 
        rawcmd = cmdparse[2].split(" ")[0]
        
        if( rawcmd.find("!") !=  -1 ):
            
            
            sender = cmdparse[1].split("!")[0]
            
            args = rawcmd.split(" ")
            command  = args[0]
            
            for val in self.cmdlist:
                
                try:
                    if(val.command.find(command)  ):
                        if(val.AcceptParams == True):
                            val.args = args
                            val.sender = sender
                            val.Execute()
                            
                        else:
                            val.args = None
                            val.sender = sender
                            val.Execute()
                      
                            
                            
                except Exception  as e:
                        print e
        
       
        rawcmd = None
        sender = None
                        
            
                        
                        
                
               
                
                
                
                    
            
                    
                
            
        
                 
        
        
                
            
        
                    
        
      
        
    
#TEST PURPOSES
    
class CommandTeste(CommandBase):
    def __init__(self, irc):
        self.irc = irc
        self.args =  []
        self.sender = ""
        CommandBase.__init__(self, "!teste", self.Execute, cmdType.CLIENT, irc, True )
       
    def Execute(self):
        print(self.args)
        print(self.sender)
        #evia pro canal
       
        self.irc.SendMessage("PRIVMSG #bittl :Ola Mundo")
        


class CommandXinga(CommandBase):
    def __init__(self, irc):
        self.irc = irc
        CommandBase.__init__(self, "!xinga", self.Execute , cmdType.CLIENT, irc, False )
       
    def Execute(self):

        #evia pro canal
       
        self.irc.SendMessage("PRIVMSG {0} :{1}".format(self.irc.clientconf.channel,  "Seu Bobo!"    )  )
        
        


