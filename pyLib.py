#Joseph Alcantara
#CMSC 128 AB-3L

#print "Nepu-Nepu"

def toWord(num, var):
	unit = numValue(num, var)
	if num != 0:

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

	else:
		var = ""

	return var + unit + " "


def numValue(num, var):
	if var == 7:
		return " million"

	elif var == 6:
		return " hundred"

	elif var == 5:
		return "ty"

	elif var == 4:
		return " thousand"

	elif var == 3:
		return " hundred"

	elif var == 2:
		return "ty"

	elif var == 1:
		return ""

def numToWord():
		#input
	var = raw_input('Enter input: ')
		# accumulator for the string
	acc = ""

		#checker if number exceeds one million
	if int(var) > 1000000:
		return "Invalid Input"
		

	while(len(var) > 0):

		acc = acc + toWord(int(var[:1]), len(var))
		var = var[1:]
	
	return acc