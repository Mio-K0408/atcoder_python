n = int(input())
total_dict = {1:[[0 for i in range(10)] for j in range(3)],2:[[0 for i in range(10)] for j in range(3)],3:[[0 for i in range(10)] for j in range(3)],4:[[0 for i in range(10)] for j in range(3)]}
for i in range(n):
    b,f,r,v = map(int,input().split())
    floor = total_dict[b]
    tmp = floor[f-1][r-1] + v
    floor[f-1][r-1] = tmp
    total_dict[b] = floor

for key,tmp_list in total_dict.items():
    for floor_list in tmp_list:
        # print(*floor_list, sep=' ')
        # print(' ', *floor_list)
        print(*[' {}'.format(e) for e in floor_list], sep='')
    if key != 4:
        print("####################")