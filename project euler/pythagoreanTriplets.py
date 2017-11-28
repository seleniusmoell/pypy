import time 

# this is a solution based on list comprehension. A good exercise, but memory heavy, t = 120s
tStart = time.time()
squares = [x**2 for x in range(1, 997)]

abc = [(x, y, z) for x in squares for y in squares for z in squares if x + y == z]


solution = [(x**0.5, y**0.5, z**0.5) for (x, y, z) in abc if x**0.5 + y**0.5 + z**0.5 == 1000]

print "Time: " + str(time.time() - tStart)
print reduce(lambda x, y: x*y, solution[0])
