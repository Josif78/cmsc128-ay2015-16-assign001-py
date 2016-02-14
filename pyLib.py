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

def basicNum(var):
    if var == "one" or var == "two" or var == "three" or var == "four" or var == "five" or var == "six" or var == "seven" or var == "eight" or var == "nine":
        return True
    return False

def specCheck(var):
    if var == "eleven" or var == "twelve" or var == "thirteen" or var == "fourteen" or var == "fifteen" or var == "sixteen" or var == "seventeen" or var == "eighteen" or var == "nineteen":
        return True
    return False

def sizeConv(var):
    num = 1

    #if var == "thousand":
     #   num = 1000
    if var == "hundred":
        num = 100

    return num

def onesConv(var):
    num = 0

    if var == "one":
        num = 1
    elif var == "two":
        num = 2
    elif var == "three":
        num = 3
    elif var == "four":
        num = 4
    elif var == "five":
        num = 5
    elif var == "six":
        num = 6
    elif var == "seven":
        num = 7
    elif var == "eight":
        num = 8
    elif var == "nine":
        num = 9
    elif var == "twenty":
        num = 20
    elif var == "thirty":
        num = 30
    elif var == "forty":
        num = 40
    elif var == "fifty":
        num = 50
    elif var == "sixty":
        num = 60
    elif var == "seventy":
        num = 70
    elif var == "eighty":
        num = 80
    elif var == "ninety":
        num = 90

    return num



def tenTwenConv(var):
    num = 0

    if var == 'ten':
        num = 10
    elif var == "eleven":
        num = 11
    elif var == "twelve":
        num = 12
    elif var == "thirteen":
        num = 13
    elif var == "fourteen":
        num = 14
    elif var == "fifteen":
        num = 15
    elif var == "sixteen":
        num = 16
    elif var == "seventeen":
        num = 17
    elif var == "eighteen":
        num = 18
    elif var == "nineteen":
        num = 19

    return num

def tailConvWN(lst):
    if len(lst) == 0:
        return 0
    else:
        retVal = 1
        unitSize = 1
        num = 0

        num = onesConv(lst[0])
        if specCheck(lst[0]):
            num = tenTwenConv(lst[0])
            lst = lst[2:]
        else:
            lst = lst[1:]

        if len(lst) > 0:
            if lst[0] == 'hundred':
                unitSize = 100
                lst = lst[1:]

                #removes thousand from the list
            if lst[0] == 'thousand':
                unitSize = unitSize * 1000
                lst = lst[1:]

                #checker for values above one thousand
            if 'thousand' in lst:
                unitSize = unitSize * 1000

        num = num * unitSize

    return num + tailConvWN(lst)

def wordToNumHelp(var):

    lst = var.split(' ')

    """i = 0
    while len(lst) > i:
        print lst[i]
        i+=1"""

    var = tailConvWN(lst)

                #regex, string to check, options
    #if re.match(r'Nepu', var, re.I):
        #var = "Nowa"

    return var

def wordToNum():
    var = raw_input('Enter input: ')

    return wordToNumHelp(var)

def currConv():
    var = raw_input('Enter input: ')

    lst = var.split(',')

    return lst[1] + str(wordToNumHelp(lst[0]))

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
        
        #while string isn't empty
    while len(lst[0]) >= denom:
        val = val + lst[0][0:denom] + splitter
        
        if len(lst[0]) == (denom):
            lst[0] = ""
            val = val[0:len(val)-1]
        lst[0] = lst[0][denom:]

    return val

