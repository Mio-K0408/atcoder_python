N,T,P = map(int,input().split())
L = list(map(int,input().split()))
# 一度ソートして、きれいにしてから考える
L.sort()

now_count = sum([a >= T for a in L])
print(0) if now_count >= P else print(T-L[-P])
# ループしなくても、境界値だけ見れば答えが出る

# 初回、無理やりループした場合
# N,T,P = map(int,input().split())
# L = list(map(int,input().split()))

# now_count = sum([a >= T for a in L])
# if now_count >= P: print(0)
# l = list(map(lambda x:x-T,L))
# count = 0

# while now_count < P:
#     l = list(map(lambda x:x+1,l))
#     now_count = sum([a >= 0 for a in l])
#     count += 1

# print(count)