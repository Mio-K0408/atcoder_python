W,H,x,y,r = map(int, input().split())
if x <=0 or y <=0:
    print('No')
elif x >= W or y >= H:
    print('No')
elif 2*r > W or 2*r > H:
    print('No')
else:
    print('Yes') 