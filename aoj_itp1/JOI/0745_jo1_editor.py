# N = int(input())
# S = input()
# ans = ''

# for i in S:
#     before_str = ans[len(ans)-1] if len(ans) != 0 else ''
#     if before_str == i:
#         ans = ans[0:-1]
#         ans += i.upper()*2
#     else:
#         ans += i

# print(ans)

N = int(input())
S = input()
ans = []

for i in S:
    if len(ans) > 0 and ans[-1] == i:
        before = ans.pop()
        ans.append(before.upper())
        ans.append(i.upper())
    else:
        ans.append(i)
print(''.join(ans))
