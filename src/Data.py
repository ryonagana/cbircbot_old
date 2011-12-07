'''
Created on 07/12/2011

@author: Nicholas
'''
import os

SRC_PATH =  os.path.abspath(os.path.dirname(__file__))
MODULES_PATH = os.path.normpath(os.path.join(SRC_PATH,'', 'modules'))



def ApplicationData(filename):
    return os.path.join(MODULES_PATH, filename)

def ApplicationDataFS(folder, filename ):
    #return os.path.join(type, filename)
    fileselected =   ApplicationData(os.path.normpath(os.path.join(folder,'', filename))) 
        
    if ( os.path.isfile(fileselected) ):
        return  fileselected