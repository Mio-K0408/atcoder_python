N = int(input())
# S = list(map(str, input().split()))

before_str = "a"
ans = "Yes"

for i in range(N):
    item = input()
    if before_str == "sweet" and before_str == item and i != N-1:
        ans = "No"
    else:
        before_str = item

print(ans)