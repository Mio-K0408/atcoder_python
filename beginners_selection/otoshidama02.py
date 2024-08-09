n, y = list(map(int, input().split()))
y = int(y/1000)
a = y%5
for i in range(n+1):
    if a == i%5:
        b = int((y-i)/5)
        c = n-i
        if b <= 2*c and b >= c:
            print(b-c, 2*c-b, i)
            exit()
print(-1, -1, -1)