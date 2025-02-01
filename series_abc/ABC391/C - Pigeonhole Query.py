N,Q = map(int,input().split())
AnsList = []
for i in range(N):
    AnsList.append({str(i):i})

for i in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 2:
        # 複数のハトがいる巣の個数を出力
        print()
    else:
        # ハトの移動
        pass

