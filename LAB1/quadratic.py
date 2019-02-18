import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
delta = (b*b) - 4*a*c
ilosc = 0
if(delta == 0):
    x1 = -b/2*a
    print("1 \n{x11}".format(x11 = x1))
    
elif(delta>0):
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print("2 \n{x11} {x22}".format(x11 = x1, x22 = x2))

else:
    print(0)
    
    
    
    
