import ConfigParser, os

class ConfigData:
    pass

class Config:
    def __init__(self, configpath):
        self.config = ConfigParser.ConfigParser()
        self.config.readfp((open(configpath)))
        
        self.path  = ""
        self.configlist = []
        self.raw =  ConfigParser.RawConfigParser()
        
        
        def Get(self,section, name):
            return self.config.get(section, name)
        
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
                
            
            
       
            
            
             
             
             
             
             
             
            
    