# -- coding: utf-8 --

import time 

# Uppgift: hitta de tal som uppfyller a**2+b**2=c**2, samt a+b+c=1000

tStart = time.time()

solution = [(x,y,1000-x-y) for x in range(1,1000) for y in range(1,x) if x**2+y**2==(1000-x-y)**2]
print "Time: " + str(time.time() - tStart)
print solution
