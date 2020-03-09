#import math
from math import sqrt  
 
a = 2
b = 2
c = 2

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print(area)