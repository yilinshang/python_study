def computepay(h,r):
    if h>40:
        return 40*r+(h-40)*1.5*r
    else:
        return h*r
    

hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rate = raw_input("Enter Rates:")
rate = float(rate)
p = computepay(hrs,rate)
print p