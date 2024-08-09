r,c = map(int,input().split())
a = []
b = []

for i in range(r):
    tmp = list(map(int,input().split()))
    total = sum(tmp)
    tmp.append(total)
    a.append(tmp)
    print(*tmp, sep=' ')
for i in range(c+1):
    count = 0
    for j in range(r):
        count += a[j][i]
    b.append(count)
print(*b, sep=' ')