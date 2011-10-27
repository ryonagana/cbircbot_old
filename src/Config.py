import ConfigParser, os

class ConfigData(object):
    pass

class Config(object):
    def __init__(self, configpath):
        self.config = ConfigParser.ConfigParser()
        
        if( os.path.isfile(configpath) == True ):
            self.config.readfp((open(configpath)))
        
        self.path  = ""
        self.configlist = []
        self.raw =  ConfigParser.RawConfigParser()
        self.clientdata = None
        
        
    def Get(self,section, name):
            return self.config.get(section, name)
        
    def GetInt(self, section, name):
            return self.config.getint(section,name)
        
    def GetFloat(self, section,name):
            return self.config.getfloat(section, name)
        
    def GetBool(self, section,name):
        return self.config.getboolean(section, name)
        
    def AddSection(self, section):
            self.raw.add_section(section)
           
            
    def AddOption(self, section,option,value):
            self.raw.set(section,option,value)
            self.configlist += [[
                                 (section,option, value)
                                 ]]
            
            
    def Write(self, filename):
            
            with open(filename, "w") as configstream:
            
                #for i in range(len(self.configlist)):
                self.config.write(configstream)
                
    def AssignClientData(self, data):
        self.clientdata = data
                
                
        
            
           
                
                            
            
            
       
            
            
             
             
             
             
             
             
            
    