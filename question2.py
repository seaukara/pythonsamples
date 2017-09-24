#-------------------------------------------------------------------------------
# Name:        Question2
# Purpose:     Write a function that takes a string as the input and return the string reversed.
#
# Author:      kara manseau
#
# Created:     24/09/2017
# Copyright:   (c) kmanseau 2017

#-------------------------------------------------------------------------------
import os
try:
    print((raw_input('Enter a string or click OK to use the default RPS Group: ') or "RPS Group")[::-1])
    os.sys.exit()
except:
       print("The cancel button was clicked - Goodbye")
       os.sys.exit()

