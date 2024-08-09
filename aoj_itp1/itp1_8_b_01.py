while True:
    num = str(input())
    if num == '0':
        exit()
    else:
        a = 0
        for i in num:
            a += int(i)
        print(a)