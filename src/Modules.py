'''
Created on 11/11/2011

@author: Nicholas
'''

import os, sys, imp

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
            print "Module Folder Found!!"
            self.modulepath =  sys.path.append(os.path.abspath(" .modules"))
            
            
        
        
        
        for key in mlist:
            try:
                modulename = os.path.basename('key')
                module = imp.load_source(key, modulename)
                
                
                if(module != None ): 
                    self.modules.append(module)
                
            except Exception as e:
                print  "module  {0} not found [{1}]".format(key, e)
            
            
        
       
        
        
        

        