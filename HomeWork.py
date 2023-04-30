import random
import math

totalThrows=100000     
throwsInsideCircle = 0
for throw in range(totalThrows): 
  x = random.random()*2 -1 
  y = random.random()*2 -1 
  if(x*x + y*y <= 1.0): 
    throwsInsideCircle += 1 


pi = (4.0*throwsInsideCircle)/totalThrows
print(pi) 
