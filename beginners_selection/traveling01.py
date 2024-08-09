from sys import stdin

N = int(input())
prev_t,prev_x,prev_y=0,0,0

for i in range(N):
    t, x, y = map(int, stdin.readline().split())
    dist = abs(x-prev_x) + abs(y-prev_y)
    if dist > t-prev_t or ((t-prev_t) % 2) !=  (dist % 2) :
        print('No')
        exit()
    prev_t,prev_x,prev_y = t, x, y

print('Yes')
