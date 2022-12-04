##
# @author Ethan Ford <ethan.ford@tuks.co,za>
 # @file Description
 # @desc Created on 2022-12-02 17:38:02
 # @copyright APPI 
 #
"""
To install Tabulate package:
https://pypi.org/project/tabulate/
or
type "pip install tabulate" in python terminal
"""
import numpy as np
from tabulate import tabulate
import cmath
import matplotlib.pyplot as plt
#==========================================

#==========================================
round_value=4
#==========================================
#Quadratic equation 
def solve (a,b,c):
    a = a
    b = b
    c = c
    
    d = (b**2) - (4*a*c)
    
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    
    print(sol1)
    print(sol2)
    
    if sol1.real<sol2.real:
        return sol1
    else:
        return sol2
#Scientific notation 
def sci(x):
    return_string='=ERROR='
    
    if (x<1):
        temp=x*1000
        if (temp>=1):
             return '{} m'.format(round(x*1000,round_value))
        temp=x*1E6
        if (temp>=1):
             return '{} µ'.format(round(x*1E6,round_value))
        temp=x*1E9
        if (temp>=1):
             return '{} n'.format(round(x*1E9,round_value))
    
    if (x>1):
        temp=x
        if (temp<1000):
             return '{} '.format(round(x,round_value))
         

        temp=x/1000
        if (temp<1000):
             return '{} k'.format(round(x/1000,round_value))
        temp=x/1E6
        if (temp<1000):
             return '{} M'.format(round(x/1E6,round_value))
        temp=x/1E9
        if (temp<1000):
             return '{} G'.format(round(x/1E9,round_value))
         
    
    return return_string    
    
#==========================================


#Write data into table for No Ls
mydata=[('round_value','{} '.format(sci(round_value))),
            ]
headers=["Parameter","Value"]
print(tabulate(mydata, headers=headers))