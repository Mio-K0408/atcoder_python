while True:
    m,f,r = map(int,input().split())
    if m == -1 and f == -1 and r == -1:
        exit()
    if -1 in (m,f):
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= m + f:
        print("B")
    elif 50 <= m + f:
        print("C")
    elif 30 <= m + f:
        if r >= 50:
            print("C")
        else:
            print("D") 
    else:
        print("F")
