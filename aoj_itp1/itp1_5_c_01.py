while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        exit()
    else:
        for height in range(H):
            if height % 2 == 0:
                if W % 2 == 0:
                    print("#."*(W//2))
                else:
                    print("{}{}".format("#."*(W//2),"#"))
            else:
                if W % 2 == 0:
                    print(".#"*(W//2))
                else:
                    print("{}{}".format(".#"*(W//2),"."))

        print()