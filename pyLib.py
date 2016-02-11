#Joseph Alcantara
#CMSC 128 AB-3L

#print "Nepu-Nepu"

def numValue(var):
	if var == 4:
		return " thousand"

	elif var == 3:
		return " hundred"

	return "ty"

def numToWord():
	var = raw_input('Enter input: ')
	while(len(var) > 0):
		var = var/10
		print "nepu" + str(var)
	
	return numValue(len(var))

print numToWord()