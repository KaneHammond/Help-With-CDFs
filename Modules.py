#########################################################
# Here we have basic imports for opening our .cdf file. #
# in order to import spacepy, you may need to use a pip #
# main command. Afterwards, you will have to install    #
# the cdf37_0_0-setup-32.exe for Windows. This is for a #
# 32 bit system. During installation it will provide a  #
# location of where it is to be installed. Below is my  #
# location, I copied this from the installer window.    #
# Yours could very well be different! Cheers!           #
#########################################################


import os
os.environ["CDF_LIB"] = "c:/CDF_Distribution/cdf37_0-dist"
import spacepy
from spacepy import pycdf
import datetime
import numpy as np

# I use this for sys.exit() this allows me to exit a script at 
# any point. Used while writing code primarily.
import sys