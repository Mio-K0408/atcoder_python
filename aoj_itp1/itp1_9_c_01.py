a,b = 0,0
n = int(input())
for i in range(n):
    t,h = input().split()
    if t < h:
        b += 3
    elif t > h:
        a +=  3
    else:
        a += 1
        b += 1

print("{} {}".format(a,b))

