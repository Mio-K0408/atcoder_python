"""
    答案1
"""
# N = int(input())
# A = list(map(int,input().split()))
# ans = 0
# for i in range(N):
#     out_loop = False
#     for j in range(i+1,N+1):
#         if out_loop:
#              break
#         tmp = A[i:j]        
#         if len(tmp) == 1:
#             ans+=1
#         elif len(tmp) == 2:
#             ans+=1
#         else:            
#             before_val = abs(tmp[1]-tmp[0])
#             updown_flag = 0 # up:1 down:-1 
#             if tmp[1] < tmp[0]:
#                     updown_flag = -1
#             elif tmp[1] > tmp[0]:
#                     updown_flag = 1
#             for x in range(2,len(tmp)):
#                 flag = False
#                 if (tmp[x] < tmp[x-1] and updown_flag == 1) or (tmp[x] > tmp[x-1] and updown_flag == -1):
#                     out_loop = True
#                     break
#                 val = abs(tmp[x]-tmp[x-1])                                
#                 if before_val == val:
#                     flag = True
#                 else:
#                     out_loop = True
#                     break
#             if flag:
#                 ans+=1
# print(ans)

"""
    答案2
"""
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0

# for i in range(N):
#     # 単一要素の部分列
#     ans += 1
#     j = i + 1
    
#     while j < N:
#         diff1 = A[j] - A[j - 1]  # 現在の差分        
        
#         # 1つ目のペアの差分を使って初期化
#         if j == i + 1:
#             previous_diff = diff1
#             updown_flag = 1 if diff1 > 0 else -1 if diff1 < 0 else 0
#             ans += 1  # 2要素の部分列もカウント
#         else:
#             # アップダウンの確認
#             if (diff1 > 0 and updown_flag != 1) or (diff1 < 0 and updown_flag != -1) or (abs(diff1) != abs(previous_diff)):
#                 break
            
#             # 正常であればカウントとフラグの更新
#             ans += 1
#             updown_flag = 1 if diff1 > 0 else -1 if diff1 < 0 else 0
#             previous_diff = diff1

#         j += 1

# print(ans)

"""
    答案3
"""
N = int(input())
A = list(map(int, input().split()))
ans = 0

i = 0
while i < N:
    ans += 1  # 単一要素の部分列もカウント
    j = i + 1
    if j < N:
        diff = A[j] - A[i]
        updown_flag = 1 if diff > 0 else -1 if diff < 0 else 0  # 初期化
        while j < N:
            current_diff = A[j] - A[j - 1]
            
            # アップダウンと差の一致を確認
            if (current_diff > 0 and updown_flag != 1) or (current_diff < 0 and updown_flag != -1) or (abs(current_diff) != abs(diff)):
                break
            
            # 条件が満たされた場合のみ
            ans += 1
            diff = current_diff
            updown_flag = 1 if diff > 0 else -1 if diff < 0 else 0
            
            j += 1
    
    # 次の部分列へ移動
    i += 1

print(ans)
