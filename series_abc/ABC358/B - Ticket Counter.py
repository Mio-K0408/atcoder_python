N,A = map(int,input().split())
T = list(map(int,input().split()))

sum = 0
pre = 0
for index,target in enumerate(T):
    """
        ansは経過時間
        ansがtargetより小さいなら、待ちがないので即購入→target+A
        ansがtargetより大きいなら、待ちがあるので1つ前の人が終わってから購入 → ans+A
    """
    ans = max(pre,target) + A
    print(ans)
    pre = ans
    
