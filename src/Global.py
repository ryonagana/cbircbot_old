'''
Created on 14/11/2011

@author: Nicholas
'''
import os, sys

modulepath = os.path.abspath(".modules")
projectfolder = os.getcwd()

sys.path.append(modulepath)
sys.path.append(projectfolder)