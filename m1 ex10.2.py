fname = input("Enter file:")
hand = open(fname)

sozdik = {}

for line in hand :
    line=line.rstrip()
    if line.startswith('From '):
        zholaq = line.split()
        uaqyt = zholaq[5]
        sagat = uaqyt[:2]
        sozdik[sagat]=sozdik.get(sagat,0)+1

for k,v in sorted (sozdik.items()) :
    print(k,v)
