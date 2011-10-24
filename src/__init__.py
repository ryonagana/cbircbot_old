
import Config
import IRCProtocol

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
    
    
    
    c = IRCProtocol.Client(data.server, data.port, data.nick, data.realname, data.email, data.ident)
    
    c.Connect()
    
    c.CreateIdentity()
    c.JoinChannel(data.channel)
    
    
    
    data = ""
   
    
    while True:
        server = []
        
        data =  c.SocketObject().recv(1024)
        c.CheckPing(data)
        server.append(data)
        
        print server[0]
        data = None
        del server
        
        
        
    
    
if __name__ == "__main__":
    main()