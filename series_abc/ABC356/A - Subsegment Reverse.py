"""
    答案1
"""
# N,L,R = map(int,input().split())
# A = []
# for i in range(1,N+1):
#     A.append(i)
# tmp = A[L-1:R]
# tmp.reverse()
# index = L-1
# for i in tmp:
#     while index < R:
#         A[index] = i
#         index+=1
#         break
# print(" ".join(map(str,A)))

"""
    答案2
"""
N,L,R = map(int,input().split())
A = list(range(1,N+1))
rev = A[L-1:R][::-1] # 該当箇所を抜き出して逆順にする
ans = A[:L-1] + rev + A[R:]
print(*ans)