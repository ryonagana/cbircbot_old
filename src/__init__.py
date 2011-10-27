
import Config
import IRCProtocol
import Module
import modules



#main entrypoint



def main():
    print "[CB-BOT by ryonagana] (for learning purposes):"
    
    
    conf = Config.Config("config.cfg")
    data = Config.ConfigData()
    
    data.nick =  conf.Get("config", "nick")
    data.email= conf.Get("config", "email" )
    data.realname = conf.Get("config", "realname")
    data.channel = conf.Get("config", "channel")
    data.server = conf.Get("config", "server")
    data.port   = conf.GetInt("config", "port")
    data.needidentify = conf.GetBool("config", "needIdentify")
    data.ident = conf.Get("config", "ident")
    
    
    
    
    if( data.needidentify == True and  data.needidentify != None  ):
        data.userpass = conf.Get("config", "password")
    else:
        data.userpass = conf.Get("config", "password")
        if ( data.userpass != None):
            print "[Warning:] Config.cfg: please clear line of your password if needIdentify is False"
    
    
    
    
    conf.AssignClientData(data)
    
    
    c = IRCProtocol.Client(data.server, data.port, data.nick, data.realname, data.email, data.ident)
    
    c.AssignConfig(conf)
    
    mod = Module.Module("config.cfg", "modules")
    
    mod.ReadAllModules()
    
    #mod.ReadList(c)
    

    
    c.Connect()
    
    c.CreateIdentity()
    c.JoinChannel(data.channel)
    
    
    
    botmessage = ""
    
    c.startUserInputThread(data)
    c.StartTimeoutThread(30)
   
    
    while True:
        server = []
        
        botmessage =  c.SocketObject().recv(1024)
        c.CheckPing(botmessage)
        server.append(botmessage)
        
        print server[0]
        botmessage = None
        del server
        
        
        
    
    
if __name__ == "__main__":
    main()