fname = input('Enter the file name : ') # file name is mbox-short.txt
try:
	fopen = open(fname,'r') # open the file to read through it
except:
	print('Wrong file name') #if user input wrong file name display 'Wrong file name'
	quit()
count = 0  # variable for number of 'X-DSPAM-Confidence:' lines
total = 0  # variable for the sum of the floating numbers

for line in fopen: # start the loop to go through file line by line
	if line.startswith('X-DSPAM-Confidence:'): # check whether a line starts with 'X-DSPAM-Confidence:'
		count = count + 1 # counting total no of lines starts with 'X-DSPAM-Confidence:'
		strip = line.strip() # remove whitespace between selected lines
		nline = strip.find(':') #find out where is ':' in selected line
		wstring = strip[nline+2:] # extract the string decimal value
		fstring = float(wstring) # convert decimal value to float
		total = total + fstring  # add the whole float values and put sum in to variable named 'total'
print('Average spam confidence:',total/count) # printout the average value
