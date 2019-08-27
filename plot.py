# -*- coding: utf-8 -*-

from mclib import *
from matplotlib import pyplot as plt
from plot import *
import subprocess

def printManifold(m,s):
    for manifold in m:
        if not "None" in manifold:
            listax = [punto.x for punto in manifold]
            listay = [punto.y for punto in manifold]
            plt.plot(listax, listay)
            name = subprocess.check_output("date",shell=True)
            name = name.decode("utf-8").rstrip()
            name = (s +" | "+
		    name[8:10] + "-" + 
                    name[4:7] + "-" + 
                    name[-4:] + "_" + 
                    name[11:19] + ".png")

            plt.savefig(name)
    
