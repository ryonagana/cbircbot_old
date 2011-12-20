'''
Created on 14/11/2011

@author: Nicholas
'''
import os, sys

modulepath = os.path.abspath(".modules")
projectfolder = os.getcwd()

sys.path.append(modulepath)
sys.path.append(projectfolder)


OWNER_PERMISSION = 999
ADMIN_PERMISSION = 450
OPERATOR_PERMISSION = 200
USER_PERMISSION = 10