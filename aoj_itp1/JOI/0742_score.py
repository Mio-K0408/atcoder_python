N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
score = 0

# for index_A in range(len(A)):
#     score += A[index_A]
#     for index_B in range(len(B)):
#         if score == B[index_B]:
#             score = 0

# print(score)

for i in A:
    score += i
    check = score in B
    if check:
        score = 0

print(score)