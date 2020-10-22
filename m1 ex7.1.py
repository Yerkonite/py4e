# Use words.txt as the file name
fname = input("Enter file name: ")
fn = open(fname)
for(fh) in fn:
    fx = fh.rstrip()
    print(fx.upper())
