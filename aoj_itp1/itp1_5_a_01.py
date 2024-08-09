while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        exit()
    else:
        for height in range(H):
            print("#"*W)
    print()