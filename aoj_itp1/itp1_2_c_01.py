a,b,c = map(int, input().split())
tmp = 0
if a < b < c:
    pass
elif a <= c <= b:
    b,c = c,b
elif b <= a <= c:
    a,b = b,a
elif b <= c <= a:
    a,b,c = b,c,a
elif c <= a <= b:
    a,b,c = c,a,b
elif c <= b <= a:
    a,b,c = c,b,a

print("{} {} {}".format(a,b,c))