X = input()
ans = ""
flg = False

for item in reversed(X):
    if flg:
        ans += item
    else:
        if item == ".":
            ans += item
            flg = False
        elif item == "0" and not ans:
            pass
        else:
            ans+=item
if ans[0] == ".":
    ans = ans[1:]
    reverse_list = list(reversed(ans))
else:
    reverse_list = list(reversed(ans))

print("".join(reverse_list))
    