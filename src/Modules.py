'''
Created on 11/11/2011

@author: Nicholas
'''

import os, sys, imp


class IModule:
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
            inst = self.loadfile(key,path)
            self.modules.append(inst)
            
            
    
    ''' 
    versao modificada  da: http://stackoverflow.com/questions/301134/dynamic-module-import-in-python
    '''
    
    def loadfile(self, classname, filepath):
        instance = None
        expected_class = classname

        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])

        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

        if expected_class in dir(py_mod):
            #instance = py_mod.__init__()
            instance = py_mod.__init__("")
            

        return instance
       
        
        
        

        