n = int(input())
num_list = list(map(int,input().split()))
num_list.reverse()
print(*num_list, sep=' ')