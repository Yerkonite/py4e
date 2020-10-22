# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
jiyn = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        strip = line.strip()
        jline = strip.find(':')
        estring = strip[jline+2:]
        fstring = float(estring)
        jiyn = jiyn + fstring
		#fn = print(line)

print("Average spam confidence:", jiyn/count)
