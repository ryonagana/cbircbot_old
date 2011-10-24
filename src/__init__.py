
import Config
import IRCProtocol

#main entrypoint

def main():
    print "CB-BOT Init:"
    
    conf = Config.Config("config.cfg")
    data = Config.ConfigData()
    
    data.nick =  conf.Get("config", "nick")
    data.email= conf.Get("config", "email" )
    data.realname = conf.Get("config", "realname")
    data.channel = conf.Get("config", "channel")
    data.server = conf.Get("config", "server")
    data.port   = conf.GetInt("config", "port")
    
    
    
    c = IRCProtocol.Client(data.server, data.port, data.nick, data.realname, data.email)
    
    c.Connect()
    c.JoinChannel(data.channel)
    c.CreateIdentity()
    
    
    
    data = ""
    
    while True:
        
        data +=  c.SocketObject().recv(1024)
        
        print data
        
        
        c.CheckPing(data)
        
        
        
    
    
if __name__ == "__main__":
    main()