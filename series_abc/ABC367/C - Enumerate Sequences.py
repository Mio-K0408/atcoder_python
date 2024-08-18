"""
    答案1（リアタイ）
    ※ 未提出
"""
# N,K = map(int,input().split())
# R = list(map(int,input().split()))
# for i in range(N-1,-1,-1):
#     list1 = [1]*N
#     if i == N-1:
#         pass
#     elif R[i] != 1:
#         list1[i] = 2
#     elif R[i] == 1:
#         continue    
#     for j in range(N-1,i-1,-1):  
#         print("{} {}".format(i,j))
#         if sum(list1) % K == 0:
#             print(" ".join(map(str,list1)))
#             tmp = list1[j]
#             list1[j] = tmp+1
#             print("{} {} {} {}".format("上",list1[j],R[j],list1))   
#             if list1[j]>R[j]:
#                 continue
#         else:
#             tmp = list1[j]
#             list1[j] = tmp+1                
#             print("{} {} {} {}".format("中",list1[j],R[j],list1)) 
#             if list1[j]>R[j]:              
#                 continue

# ------------------------------------------
"""
    答案2
    再帰法（繰り返しよりメモリ使用量が多く、速度も遅い）
"""
N,K = map(int,input().split())
R = list(map(int,input().split()))

def f(n, arr, s):
    if n == N:
        if s % K == 0:
            print(' '.join(map(str, arr)))
        return
    for i in range(1, R[n]+1):
        f(n+1, arr+[i], s+i)

f(0, [], 0)
