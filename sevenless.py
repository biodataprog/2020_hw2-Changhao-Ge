#!/usr/bin/env python3

start = 0
end   = 99
divisor=7
number=start
print("Printing out numbers from",start,"to",end, " not divisible by",divisor)
for n in range(start,end+1):
 if(n % divisor != 0):
  print(n)

  