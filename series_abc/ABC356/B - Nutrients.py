N,M = map(int,input().split())
A = list(map(int,input().split()))
sum_check = [0]*M
for i in range(N):
    X = list(map(int,input().split()))
    for j in range(M):
        tmp = sum_check[j]
        sum_check[j] = tmp + X[j]

for index,item in enumerate(sum_check):
    if item >= A[index]:continue
    else:
        print("No")
        exit()

print("Yes")