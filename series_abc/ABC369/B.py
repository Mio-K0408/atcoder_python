"""
    答案1
"""
N = int(input())
ans = 0
L = 0
R = 0
for i in range(N):
    A,S = input().split()
    if S=="L" and L==0:
        L = int(A)
    elif S=="R" and R==0:
        R = int(A)
    else:
        if S == "L":
            ans += abs(L-int(A))
            L = int(A)
        elif S == "R":
            ans += abs(R-int(A))
            R = int(A)

print(ans)