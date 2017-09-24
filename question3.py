#-------------------------------------------------------------------------------
# Name:        Question 3
# Purpose:     Write a function that takes in a number and return the closes multiple of 7 to that number. Example: input 15 return 14. Input 19 return 21.

#
# Author:      kmanseau
#
# Created:     24/09/2017
# Copyright:   (c) kmanseau 2017

#-------------------------------------------------------------------------------
import os, math

label = "Please enter a number"+ "/n or click OK to use default value of 15: "
try:
    x = float(raw_input("Enter a # or click OK to use default of 15: ") or 15.0)
except:
       print("Cancel button was clicked - Goodbye")
       os.sys.exit()
if (x - (7* math.floor(x/7))) <= (7* math.ceil(x/7) - x):
 print(int(7* math.floor(x/7)))
else:
   print(int(7* math.ceil(x/7)))

del x
os.sys.exit()
