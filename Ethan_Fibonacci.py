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
FibonacciArray=0

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
print("The number of digits in the number are:",getDigits(n))




