xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
xc,yc = map(int,input().split())

ab2 = (xa-xb)**2 + (ya-yb)**2
ca2 = (xa-xc)**2 + (ya-yc)**2
bc2 = (xb-xc)**2 + (yb-yc)**2

if ab2 + ca2 == bc2 or ab2 + bc2 == ca2 or bc2 + ca2 == ab2:
    print('Yes')
# elif ab2 + bc2 == ac2:
#     print('Yes')
# elif bc2 + ac2 == ab2:
#     print('Yes')
else:
    print('No')
