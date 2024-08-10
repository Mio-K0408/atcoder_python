N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)
max2 = A_sorted[N-2]
# count = 0
# max_num = 0
# max_num2 = 0
# for index, num in enumerate(A):
#     if index == 0:
#         max_num = num  
#     elif index == 2:
#         if max_num > num:
#             max_num2 = num
#         else:
#             max_num2 = max_num
#             max_num = num
#     if max_num2 > num:
#         pass
#     elif max_num < num:
#         max_num2 = max_num
#         max_num = num
#     elif max_num > num > max_num2:
#         max_num2 = num


print(A.index(max2) + 1)