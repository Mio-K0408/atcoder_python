N = int(input())
A = list(map(int,input().split()))
count = 0
target = A[0]
tmp = 0
for index in range(2*N-2):
    if A[index] == A[index+2]:
        count+=1
print(count)