import math

x1,y1,x2,y2 = map(float,input().split())
x = (x2-x1)**2
y = (y2-y1)**2
dis = x + y
print(math.sqrt(dis))
