#import RPi.GPIO as GPIO
import time
def ToString (List): # Coverts List to String
    return ''.join(List)
def Setup ():
def Wait ():
    reading_file=open('DataStore.txt', 'r')
    lines=reading_file.readlines()
    #print lines
    GoodLine = lines[len(lines) - 1] #GoodLine is the last line of the file!
    if len(lines) > len(oldLinesGood): # If there are more lines in the new one one was added. So then that line should be read
        return True
    else:
        return False
    OldGood = GoodLine # Resets Vars For comparison
    oldLinesGood = lines
