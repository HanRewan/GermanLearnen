from DictCore import *
import sys
import os

DP = DictParser()
DP.unRawDoc(os.getcwd() + '/' + sys.argv[1])