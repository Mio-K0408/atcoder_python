import math
a,b,c = map(int,input().split())
C = math.radians(c)
s = 1/2*a*b*(math.sin(C))
c = math.sqrt(a**2 + b**2 -(2*a*b*math.cos(C)))
l = a+b+c
h = 2*s / a
print("{:.8f}".format(s))
print("{:.8f}".format(l))
print("{:.8f}".format(h))