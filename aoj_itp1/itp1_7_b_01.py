while True:
    n,x = map(int,input().split())
    count = 0
    if n == 0 and x == 0:
        exit()
    else:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for z in range(j+1,n+1):
                    if i + j + z == x:
                        count += 1                        
        print(count)