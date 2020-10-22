fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
#collection = fh.read()
wordlist = list()

for line in fh:
    if not line.startswith("From ") : continue
    if line.startswith("From ") :
        count = count + 1
        line = line.strip()
        words = line.split()
    if len(words) < 3 :
        continue
    value = words[1]
    print(value)
        #wordlist.append(value)
#        wordloop = wordlist.rstrip()

#for wordloop in collection:
#    wordloop = wordloop.rstrip()
#    if not wordloop.startswith("From ") :
#        continue
#	if wordloop.startswith("From ") :
#        words = wordloop.split()
#       value = words[2]
#        wordlist.append(value)

#for wordloop in collection.split():
    #wordloop = wordloop(r)
    #if wordloop.startswith("From ") :
    #value = wordloop[1]
    #wordlist.append(value)
    #if value in wordlist:
     #   continue
    #wordlist.append(value)

#print(wordlist)
print("There were", count, "lines in the file with From as the first word")
