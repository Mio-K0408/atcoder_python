i = 1
while True:
    x,y = map(int, input().split())
    if x == 0 and y == 0:
        exit()
    else:
        if x > y:
            x,y = y,x
        print("{} {}".format(x,y))