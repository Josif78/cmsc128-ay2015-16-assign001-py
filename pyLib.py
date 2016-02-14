#Joseph Alcantara
#CMSC 128 AB-3L

#!/usr/bin/python
import re
#print "Nepu-Nepu"
    
    #function that converts integers to strings
def toWord(num, var):   
    sen = False
    if var == 4:
        sen = True
	   
       #checks if current number is zero
        #skips if a zero is detected
    if num != 0:
        if var == 2 or var == 5:
            var = toTens(num)

        else:
            unit = numValue(var)

            if num == 9:
                var = "nine"

            elif num == 8:
                var = "eight"

            elif num == 7:
                var = "seven"

            elif num == 6:
                var = "six"

            elif num == 5:
                var = "five"

            elif num == 4:
                var = "four"

            elif num == 3:
                var = "three"

            elif num == 2:
                var = "two"

            elif num == 1:
                var = "one"

            var = var + unit
    else:
        var = ""

        #appends thousand value to the end of the string
    if sen:
        if var != 0:
            var = var + " "
        var = var + "thousand "

    return var

    #function that returns the tens value
def toTens(num):
    var = ""

    if num == 1:
        var = "ten"
    elif num == 2:
        var = "twenty"
    elif num == 3:
        var = "thirty"
    elif num == 5:
        var = "fifty"
    elif num == 8:
        var = "eighty"
    else:
        var = toWord(num, 1) + "ty"

    return var + " "

    #function for checking the value of the unit
def numValue(var):
    if var == 7:
        return " million "

    elif var == 6 or var == 3:
        return " hundred "

    elif var == 4 or var == 1:
        return ""

    #function for special cases between ten and twenty
def tenToTwenty(num, var):
    if num == 1:
        num  = "eleven"

    elif num == 2:
        num  = "twelve"

    elif num == 3:
        num  = "thirteen"

    elif num == 4:
        num  = "fourteen"

    elif num == 5:
        num  = "fifteen"

    elif num == 6:
        num  = "sixteen"

    elif num == 7:
        num  = "seventeen"

    elif num == 8:
        num  = "eighteen"

    elif num == 9:
        num  = "nineteen"

    if var == 5:
        num = num + " thousand"

    return num + " "

        #word-ize
def numToWord():
        #input
    var = raw_input('Enter input: ')
        # accumulator for the string
    acc = ""

        #checker if number exceeds one million
    if int(var) > 1000000:
        return "Invalid Input"  	

    while(len(var) > 0):
        if ((len(var) == 5 or len(var) == 2) and (int(var[:1]) == 1 and int(var[1:2]) > 0)):
            #print "Nowaru"
            acc = acc + tenToTwenty(int(var[1:2]), len(var))
            var = var[2:]

        else:
            acc = acc + toWord(int(var[:1]), len(var))
            var = var[1:]

    return acc

def tailConvWN(acc, var):

    if var != '@':
        acc = acc + tailConvWN(acc, var)
    return acc

def wordToNum():
    var = raw_input('Enter input: ')

    acc = ""

    if re.match( r'Nepu', var, re.I):
        var = "Nowa"

    return var

def delimit():
    var = raw_input('Enter input: ')

        #split into list
    lst = var.split(',')

        #checker if value exceeds one million
    if int(lst[0]) > 1000000 or len(lst[2]) > 3:
        return "Invalid Input"

        #checker for splitter character
    if len(lst[2]) != 3:
        splitter = ',';
    else:
        splitter = lst[2][1:2]

    val = "" #accumulator for the value to be printed
    denom = int(lst[1]) #number of jumps to be split
    numSize = len(lst[0]) #size of the initial number
    jumps = (numSize % denom) #number of jumps for the first split

    if numSize < denom:
        return "Invalid Input"

        #if the number cannot be perfectly divided by the number of jumps
    if jumps > 0:
        val = lst[0][0:jumps] + splitter
        lst[0] = lst[0][jumps:]
        
        #
    while len(lst[0]) >= denom:
        val = val + lst[0][0:denom] + splitter
        
        if len(lst[0]) == (denom):
            lst[0] = ""
            val = val[0:len(val)-1]
        lst[0] = lst[0][denom:]

    return val

