N = int(input())
A = map(int, input().split())

ans = []
for a in A:
    if a not in ans:
        ans.append(a)
    else:
        ans.remove(a)

print(ans[0])
