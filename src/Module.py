from src import Config
import os


class ModuleClass:
    pass


class Module(object):
    def __init__(self, config, folder):
        self.conf = Config.Config(config)
        self.folder = os.path.basename(folder)
        self.modulelist = []
        self.moduleInstance = []
        
    def ReadList(self):
        
        getlist = ""
        
        getlist = self.conf.Get("modules", "modules")
        
        if (getlist == None):
            return 0
        
        list = getlist.split(",")
        
        for i in range(len(list)):
            self.modulelist.append(list[i])
            
            try:
                self.moduleInstance[i] = __import__(list[i])
                print "Modules Loaded: {0} ".format(list[i])
                break
            except  Exception:
                print "Error on load Module: [ {0} ]".format(list[i])
                  
        
        
        def  InitPlugins(self):
            
            for i in range(len(self.moduleInstance)):
                self.moduleInstance[i].__init__()
        
        
        
        
        
        
    