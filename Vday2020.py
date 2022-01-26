# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:57:23 2020

@author: daisy
"""
"""
thinking :
    1. all the letters showed by math graghs 
    2. interactive: type names(me and my husband)
    3. say something , simple 
    4. type i love you and happy 'whatever' day (here is v day)
    5. animated (page with grides(6,n), math graphs show )
    6. seal in an app
"""
import math as math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1=np.linspace(0,2*np.pi,100)
data2=np.linspace(np.pi,2*np.pi,100)
c='b'

# this is the letter O
def LO(i,j,c):
    data1
    axs[i,j].plot(3*np.cos(data1),3*np.sin(data1),c=c)
    axs[i,j].axis('off')

    
 # this is the letter I   
def LI(i,j,c):
    axs[i,j].plot(range(1,4),[5,5,5],c=c)
    axs[i,j].plot(range(1,4),[0,0,0],c=c)
    axs[i,j].plot([2,2,2,2,2,2],range(6),c=c)
    axs[i,j].axis('off')


# this is the letter J
def LJ(i,j,c):
    axs[i,j].plot(range(1,4),[5,5,5],c=c)
    axs[i,j].plot([2,2,2,2,2,2,2,2,2,2],[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5],c=c)
    axs[i,j].plot(1+np.cos(data2),0.5+np.sin(data2),c=c)
    axs[i,j].axis('off')


