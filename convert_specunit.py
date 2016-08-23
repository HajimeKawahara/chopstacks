#!/usr/bin/python
import sys
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *

def q2rsunit(wav,wavw,f):

    if len(wav)+1==len(wavw) and len(wav)==len(f):
        for i in range(0,len(wav)):
            f[i]=f[i]/(wavw[i+1]-wavw[i])                
        return f
    else: 
        print "ERROR: Length is inconsistent"
        print "len(wav),len(wavw),len(f)"
        print len(wav),len(wavw),len(f)
        sys.exit("stop")


def rsunit2q(wav,wavw,f):
    
    if len(wav)+1==len(wavw) and len(wav)==len(f):
        for i in range(0,len(wav)):
            f[i]=f[i]*(wavw[i+1]-wavw[i])            
        return f
    else: 
        print "ERROR: Length is inconsistent"
        print "len(wav),len(wavw),len(f)"
        print len(wav),len(wavw),len(f)
        sys.exit("stop")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Convert the spectra to that with the [q/X] unit (rsunit), which is the redstack fiducial unit.')

