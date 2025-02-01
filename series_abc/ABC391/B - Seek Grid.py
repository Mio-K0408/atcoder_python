N,M = map(int,input().split())

S = []
for i in range(N):    
    S.append(input())

T = []
for i in range(M):    
    T.append(input())

Toutercount = 0
Tinnercount = 0
check_flag = False
for i in range(N-M+1):
    if not check_flag:
        for j in range(N-M+1):
            strS = S[i]
            strT = T[i]
            if strS[j:j+N-M+1] == strT[0:M]:
                if M !=1 and i != M:
                    strS = S[i+1]
                    strT = T[i+1]
                    if strS[j:j+N-M+1] == strT[0:M]:
                        check_flag = True
                        print('{} {}'.format(str(i)),str(j))
                        break
                    else:
                        print('{}:{}'.format(strS[j:j+N-M+1],strT[0:M]))
                        print('{}:{}'.format(str(j),str(N-M)))
                elif M == 1:
                    check_flag = True
                    print('{} {}'.format(str(i)),str(j))
                    break
            else:
                print('{}:{}'.format(strS[j:j+N-M+1],strT[0:M]))
                print('{}:{}'.format(str(j),str(N-M)))
        
        