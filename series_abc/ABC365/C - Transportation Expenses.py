N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if M >= sum(A):
    print('infinite')
else:
    MAX = M
    MIN = 0
    while MAX - MIN > 1:
        a = 0
        for i in range(N):
            a += min(A[i], MAX)
            if a > M:
                MAX -= 1
                break
            else:
                pass
        if a > M:
            continue
        else:
            print(MAX)
            exit()

# amount = 0
# count = 0
# max = A[0]
# while True:
#     for index, num in enumerate(A):        
#         amount += min(max,num)
#     if M >= amount:
#         print(max)
#         exit()
#     else:
#         amount = 0
#         count += 1
#         max = A[count]
    
# min_A = int(M / N)
# A_sorted = sorted(A)
# A_max = A_sorted[N-1]
# amount = 0

# for num in A:
#     ret = min(min_A, num)
#     amount += ret


# if M >= amount:
#     if min_A>A_max:
#         print('infinite')
#     else:
#         print(min_A)