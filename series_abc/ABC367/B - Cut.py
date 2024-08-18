"""
    答案1（リアタイ）
"""

# X = input()
# ans = ""
# flg = False

# for item in reversed(X):
#     if flg:
#         ans += item
#     else:
#         if item == ".":
#             ans += item
#             flg = False
#         elif item == "0" and not ans:
#             pass
#         else:
#             ans+=item
# if ans[0] == ".":
#     ans = ans[1:]
#     reverse_list = list(reversed(ans))
# else:
#     reverse_list = list(reversed(ans))

# print("".join(reverse_list))

# ------------------------------------------
"""
    答案2
    言語の機能である、型変換を使う
    ※ 言語仕様によるので他の解法も知っておくほうがいい。
"""
# x = float(input())
# # is_integer():整数か判定（小数点以下が0）
# # int():int型に変換、
# if (x.is_integer()):
#   print(int(x))
# else:
#   print(x)
    
# ------------------------------------------
"""
    答案3
    文字列として扱い、不要な文字を削除していく。
    言語仕様によらないので、どの言語でも使える。
"""
X = input()

while X[-1] == "0":X=X.rstrip("0")
if X[-1] == ".":X=X.rstrip(".")
print(X)