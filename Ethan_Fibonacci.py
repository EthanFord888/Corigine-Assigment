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
#==========================================
#Variables 
F=[0,1,1]
digits=1
index = 2
#==========================================
#Determine number of digits
def getDigits(x):
     count = 0
     while(x>0):
          count=count+1
          x=x//10
     return count

#==========================================
n=int(input("Enter number:"))
while (n!= digits):
     F[0]=F[1]+F[2]
     digits=getDigits(F[0])
     index+=1

     F[2]=F[1]
     F[1]=F[0]
     
print("The number of digits in the number are:",index)





