'''
Created on 27/10/2011

@author: Nicholas
'''
from distutils.core import setup
from py2exe import *
import sys

sys.path.append("../");
sys.path.append("../src/")

setup(console=['../src/__init__.py'])