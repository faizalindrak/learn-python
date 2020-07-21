def computepay(h,r):
    if h > 40:
        pay = (h*r) + ((h-40)*0.5*r)
        return pay
    else:
        pay = h*r
        return pay
              
hrs = input("Enter Hours:")
rate = input("Enter rate: ")
try:
    fh=float(hrs)
    fr=float(rate)
except:
    print("please input numeric")
   
p = computepay(fh,fr)
print("Pay",p)