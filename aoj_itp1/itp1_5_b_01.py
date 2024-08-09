while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        exit()
    else:
        for height in range(H):
            if height == 0 or height == H-1:
                print("#"*W)
            else:
                print("{}{}{}".format("#","."*(W-2),"#"))
        print()