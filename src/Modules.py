'''
Created on 11/11/2011

@author: Nicholas
'''

import os, sys, imp
import Data
import modules
import Global


class IModule:
    def __init__(self):
        
        self.cmdname = ""
        self.args = []
        self.sender = ""
        self.channelsent = ""
        self.permission = Global.USER_PERMISSION

        
        
    def Execute(self):
        pass
    
    



class Modules(object):

    def __init__(self, config):
        self.config = config
        self.modulenames = []
        self.modules= []
        self.moduleinstances = []
        self.modulepath = None
        
        
        mlist = self.config.modules.split(",")
        
        #checar se a pasta modules existe
            
        if(os.path.isdir(Data.MODULES_PATH) == False  ):
            print ".modules not found"
            exit(1)
        else:
            sys.path.append(os.getcwd())
            self.modulepath =  Data.MODULES_PATH
            
            
        
        
        
        for key in mlist:
            path = Data.ApplicationData("{0}.py".format(key))
            self.loadfile(path)
            #self.modules.append(inst)
            
    
    ''' 
    versao modificada  da: http://stackoverflow.com/questions/301134/dynamic-module-import-in-python
    '''
    
    def loadfile(self, filepath):
        try:
            module_dir, module_file = os.path.split(filepath)
            module_name, module_ext = os.path.splitext(module_file)
            module_fullpath = filepath
            module_obj = None
            save_cwd = os.getcwd()
            os.chdir(module_dir)
            
            
            if(module_fullpath.find(".py") ): 
                module_obj =  imp.load_source(module_name, module_fullpath)
            elif (module_fullpath.find(".pyc")):
                module_obj = imp.load_compiled(module_name, module_fullpath)
            
            
            
            
            #module_obj = __import__("module." + module_name)
            module_obj.__file__ = module_fullpath
            #globals()[module_name] = module_obj
            #self.modules.append(module_obj.__class__)
            #module_compiled = imp.load_compiled(module_name, module_fullpath)
            
            comp = module_fullpath.split('.')
            
            for c in comp[1:]:
                module_attr = getattr(module_obj,module_name)
                
            
            self.modules.append(module_attr)
            self.modulenames.append(module_name)
            

            
            
        except:
            raise ImportError
        
        return module_attr
    
    def RunModules(self, client):
        
        if( len(self.modules) != 0 ):
            
            for module in self.modules:
                self.moduleinstances.append( module(IModule, self.config, client ))
                

            
            
            
            
                
                
            
        
    

       
        
        
        

        