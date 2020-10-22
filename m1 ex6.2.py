data = "X-DSPAM-Confidence:    0.8475";
atpos = data.find(':')
sppos = data.find('5')
numba = data[atpos+1 : sppos+1]
number = float(numba)
print(number)
