N,K = map(int,input().split())
R = list(map(int,input().split()))
for i in range(N-1,-1,-1):
    list1 = [1]*N
    if i == N-1:
        pass
    elif R[i] != 1:
        list1[i] = 2
    elif R[i] == 1:
        continue    
    for j in range(N-1,i-1,-1):  
        print("{} {}".format(i,j))
        # if flg:
        if sum(list1) % K == 0:
            print(" ".join(map(str,list1)))
            tmp = list1[j]
            list1[j] = tmp+1
            print("{} {} {} {}".format("上",list1[j],R[j],list1))   
            if list1[j]>R[j]:
                continue
        else:
            tmp = list1[j]
            list1[j] = tmp+1                
            print("{} {} {} {}".format("中",list1[j],R[j],list1)) 
            if list1[j]>R[j]:              
                continue
        # else:
        #     print("抜ける")
        #     break

