S,T = input().split()

for w in range(1,len(S)): # w文字区切り
    for c in range(w):
        now = ""
        for i in range(c,len(S),w): # 長さがc以上、c文字目を連結         
            now += S[i]
        if now == T:
            print("Yes")
            exit()
print("No")
