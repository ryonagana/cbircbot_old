'''
Created on 11/11/2011

@author: Nicholas
'''

import os, sys, imp


class IModule:
    def __init__(self):
        pass
        
    def Execute(self):
        pass



class Modules(object):

    def __init__(self, config):
        self.config = config
        self.modulenames = []
        self.modules= []
        self.modulepath = None
        
        
        mlist = self.config.modules.split(",")
        
        #checar se a pasta modules existe
            
        if(os.path.isdir( os.path.abspath(".modules")) == False  ):
            print ".modules not found"
            exit(1)
        else:
            sys.path.append(os.getcwd())
            self.modulepath =  sys.path.append(os.path.abspath(" .modules"))
            
            
        
        
        
        for key in mlist:
            path = os.path.abspath(".modules/{0}.py".format(key)) 
            inst = self.loadfile(path)
            self.modules.append(inst)
            
    
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
            module_obj =  imp.load_source(module_name, module_fullpath)
            #module_obj = __import__(module_fullpath)
            module_obj.__file__ = module_fullpath
            globals()[module_name] = module_obj
            os.chdir(save_cwd)
            
        except:
            raise ImportError
        
        return module_obj.__class__

       
        
        
        

        