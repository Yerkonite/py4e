hrs = input("Enter Hours:")
rt = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rt)
except:
    print("Error. Numeric is needed")
    quit()
if h < 40:
    pay = h*r
elif h > 40:
    pay = 40*r + (h-40)*r*1.5
m = float(pay)
print(m)
