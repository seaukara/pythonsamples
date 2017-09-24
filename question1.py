#-------------------------------------------------------------------------------
# Name:        Question 1
# Purpose:     Write code that prints the numbers from 1 to 100. For multiples of three print "RPS" instead of the number and for the multiples of five print "Group". For numbers which are multiples of both three and five print "RPS Group".

#
# Author:      kara manseau
#
# Created:     24/09/2017
# Copyright:   (c) kmanseau 2017

#-------------------------------------------------------------------------------

def printNumber(currentNumber):

    if currentNumber%3 == 0 or currentNumber%5 == 0:
       if currentNumber%5 > 0:
          print("RPS")
       elif currentNumber%3 > 0:
            print("Group")
       else:
        print("RPS Group")
    else:
         print(currentNumber)

    del currentNumber
    return

if __name__ == '__main__':
   import os

   for i in range(1, 101):
       printNumber(i)
   print("\nCompleted - Goodbye")
   os.sys.exit()