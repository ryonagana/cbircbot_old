from src import Config

import os, sys, imp
from modules import *

class ModuleClass:
    def __init__(self,  ircprotocol):
        self.irc = ircprotocol
        
        


class Module(ModuleClass):
    def __init__(self, config, folder):
        self.conf = Config.Config(config)
        self.folder = os.path.basename(folder)
        self.modulelist = []
        self.moduleInstance = dict()
        
    def AddModule(self, cmd, func ):
        
        try:
            self.moduleInstance[cmd] =  func
        except Exception as e:
            print "Module Invalid {0}".format(e)
    
    def ReadAllModules(self):
        
        getmodules = self.conf.Get("modules","modules")
        modules = getmodules.split('",')
        
        for i in range( len(modules)):
            
            try:
                self.AddModule(modules[i], __import__("modules." + modules[i]))
                self.moduleInstance[i].__init__(self.irc)
            except Exception as e:
                print "Cannot Create Module:{0}".format(e)
        
      
            
            
            
        
        
        
        
        
        
    