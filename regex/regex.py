# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re
fname = input("Enter file:")
hand = open(fname)
y = []
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        y = y + x
jiyn = 0
for z in y:
    jiyn = jiyn + int(z)

print(jiyn)