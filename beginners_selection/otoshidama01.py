n,y = map(int, input().split())
a,b,c = -1,-1,-1
check_flg = False

for i_c in range(0,n+1):
    for i_b in range(0,n+1):
        for i_a in range(0,n+1):
            total = 10000*i_a + 5000*i_b+ 1000*i_c            
            if total == y:
                if n == i_a + i_b + i_c:
                    a,b,c = i_a,i_b,i_c
                    break
                else:
                    if check_flg:
                        break

            else:
                if check_flg:
                    break


print("{} {} {}".format(a,b,c))