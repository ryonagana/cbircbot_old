from src import Config

import os, sys, imp
from modules import *

class ModuleClass:
    def __init__(self,  ircprotocol):
        self.irc = ircprotocol
        
        


class Module(object):
    def __init__(self, config, folder):
        self.conf = Config.Config(config)
        self.folder = os.path.basename(folder)
        self.modulelist = []
        self.moduleInstance = []
        
    def ReadList(self, ircclass):
        
        mlist = self.conf.Get("modules", "modules")
        aux =  mlist.split(',')
        
        
        for i in range ( len(mlist) ):
            aux.append(aux[i])
                      
            try:
                self.moduleInstance[i] = __import__("modules.{0}".format(aux[i]))
                 
            except Exception as (e):
                print "Error: {0}".format(e)
                
        
               
     
             
        
    def  InitPlugins(self, ircclass):
            
            for i in range(len(self.moduleInstance)):
                self.moduleInstance[i].__init__(ircclass)
        
        
        
        
        
        
    