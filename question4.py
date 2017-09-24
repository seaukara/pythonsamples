#-------------------------------------------------------------------------------
# Name:        Qestion 4 & 4a & 4b
# Purpose:     Write a function that removes duplicate characters from the string passed in and return the rest. Please keep the first instance of the duplicate character in the output string.? Example:? Pass in ?Ball? Output: ?Bal?? Example 2: Pass in ?AABBCC? output: ?ABC?. Bonus points if you can get "RPS Group" to come back as "RPS Gou" using your method from question 4 above. Bonus points if you can tell me why 4a might be a challenge.?

#
# Author:      kara manseau
#
# Created:     24/09/2017
# Copyright:   (c) kmanseau 2017

#-------------------------------------------------------------------------------

def removeDuplicates(phrase):
    uniqueCharater = ""
    for letter in phrase:
        if letter not in uniqueCharater:
           uniqueCharater = uniqueCharater + letter
    return uniqueCharater

def removeDuplicates_caseIgnored(phrase):
    uniqueCharater = ""
    for letter in phrase:
        if letter.lower() not in uniqueCharater.lower():
           uniqueCharater = uniqueCharater + letter
    return uniqueCharater

if __name__ == '__main__':
   import os
   try:
       phrase = raw_input("Enter a string or click OK to use default of RPS Group: ") or "RPS Group"
   except:
          print("Cancel button was clicked - Goodbye")
          os.sys.exit()
   caseSensitive = removeDuplicates(phrase)
   print("Question 4: " + caseSensitive)

   caseInsensitive = removeDuplicates_caseIgnored(phrase)
   print("Question 4a: " + caseInsensitive)

   if caseSensitive != caseInsensitive:
      print("Question 4b: The results are different for 4 & 4a becuase the input phrase used multiples of the same letter with different case sensitivities.\nThe logic of the code does not inheriently see these charaters as different, so it must be explicitly specified that case should be ignored.")
   else:
        print("Question 4b: The results are the same becuase there are no duplicate characters with different cases.")
   os.sys.exit
