'''
Created on 28/10/2011

@author: Nicholas
'''
import IRCProtocol

class CommandType:
    pass



cmdType = CommandType()
cmdType.SERVER = 1
cmdType.CLIENT = 2
cmdType.INVALID = 0 


class CommandBase(object):
    def  __init__(self, name, func_class, typecmd, ircprotocol ):
        self.command = name
        self.args =  None
        self.func = func_class
        self.type = typecmd
        self.irc = ircprotocol
    
    def Execute(self):
        pass
    
    
class CommandList(object):
    def __init__(self, irc):
        self.cmdlist = []
        
        self.cmdlist.append(CommandTeste(irc))
        
        
    def CommandParser(self, command):
        
        '''
            if( command.find("!") != -1 ):
                separate  = command.split("!")
            
            
            
                for i in range(len(self.cmdlist)):
                    if( self.cmdlist[i].command == command):
                    
                        parse = separate[1].split(" ")
                    
                        for j in range(len(parse)):
                            self.cmdlist[j].args.append(parse[j])
                    
                        self.cmdlist[i].Execute()
                    
                    
        '''
        
        #texto = command.split(" ")
        
        #if (texto[3].find("!") != -1 ): # if message contains ! is a command!! (check only is a command) now we check if is a valid command
        
        '''if ( command.find("!") != -1 ):
            parseCommand = texto[3].split(":")
                
                for i in range(len(self.cmdlist)):
                    if (parseCommand == self.cmdlist[i].command):
                        
                        args = parseCommand.split(" ")
                        
                        for j in range (len(args)):
                            self.cmdlist[i].args.append(args[j])
                            
                        self.cmdlist[i].Execute()
                        
        else:
            print "Command Invalid"
            
        '''
        #TESTS
        message = command.split(":")
        if message[1].find("!") != -1:
            
            for val in self.cmdlist:
                if( message[1] ==  val.command):
                    print "Comando Existe"
                else:
                    print "Comando Nao existe"
                
                
                
            
        
                    
        
      
        
    
#TEST PURPOSES
    
class CommandTeste(CommandBase):
    def __init__(self, irc):
        self.irc = irc
        CommandBase.__init__(self, "!teste", self.Execute() , cmdType.CLIENT, irc )
       
    def Execute(self):
        print "hello World!"
        #evia pro canal
       
        self.irc.Talk("aaaaa", "#chapolin" )
        
        
