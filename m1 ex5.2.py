largest = -1
smallest = 11
while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    if fnum > largest :
        largest = int(fnum)
    elif fnum < smallest :
        smallest = int(fnum)

    #print(fnum)

print('Maximum is', largest)
print('Minimum is', smallest)
