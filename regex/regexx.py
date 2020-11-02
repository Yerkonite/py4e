import re

fname = input("Enter file:")
hand = open(fname)
numlist = list()

for line in hand:
    stuff = re.findall('[0-9]+', hand)
    num = float(stuff)
    numlist.append(num)
    #line = linregex_sum_42e.split()
    #lst.append(line)


print('The sum is ', sum(numlist))