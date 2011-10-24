'''
Created on 24/10/2011

@author: Nicholas
'''

import urllib2
from xml.dom import minidom, Node
import xml.dom

class RSSFeeder(object):

    def __init__(self):
        self.urlobject = None
        self.dom = None
        self.rootnode = None
        

    def OpenURL(self, url):
        self.urlobject = urllib2.urlopen(url)
        self.dom  =  minidom.parse(self.urlobject)
        self.rootnode = self.dom.documentElement
        

                
        
        
        
        
        
        
    
    
    
        