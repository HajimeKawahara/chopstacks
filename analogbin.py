#!/usr/bin/python
import sys
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
import chopstacks as cs

def set_master_analog(xs,xe,R,opt):
    # it might be useful to set the master analog bin.
    # xs & xe should be x[0] & x[-1] 
    if(opt==0):
        ls=np.log(xs)
        le=np.log(xe)
        Nf=R*(le-ls)
        Ni=int(Nf)
        logx=np.linspace(ls,le,Ni)
        hxw=cs.buildwall(logx)
        hxw=exp(hxw)
        hx=exp(logx)
        
        return hx, hxw

    elif(opt==1):
        ls=np.log(xs)
        le=np.log(xe)
        Nf=R*(le-ls)
        Ni=int(Nf)
        lhx=np.linspace(ls,le,Ni)
        lhxw=cs.buildwall(lhx)

        return lhx, lhxw

    else:
        print "no opt @ set_master_analog"
        sys.exit("exit")

def setanalogbin(x,xw,f,R,opt=0):
    # opt=1 gives log(x) and log*x*f instead of x, f

    if(opt==0):
        hx,hxw=set_master_analog(x[0],x[-1],R,opt)
        hf=cs.cutput(xw,f,hxw)

        return hx, hxw, hf

    elif(opt==1):
        lhx,lhxw=set_master_analog(x[0],x[-1],R,opt)
        hxf=cs.cutput(np.log(xw),x*f,lhxw)
        
        return lhx, lhxw, hxf


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Re-Binning spectra with the unit of [q/X] to the logarithm bin.')

    nwav=1000
    ws=400.0
    we=1000.0
    wav=np.linspace(ws,we,nwav)
    wavw=cs.buildwall(wav)
    f=np.random.normal(0.0,1.0,nwav)+(np.linspace(1.0,4.0,nwav))**2.0

    R=100.0
    hx, hxw, hf=setanalogbin(wav,wavw,f,R,0)
    cs.check_preservation(wavw,f,hxw,hf)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(wav,f,color="blue")
    ax.plot(hx,hf,"o",color="red")
    xlabel("$x$")
    ylabel("$f$ (blue), $\hat{f}$ (red)")
    plt.show()
    
