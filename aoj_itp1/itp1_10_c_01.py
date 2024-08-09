import statistics

while True:
    n = int(input())
    point_list = []
    if n == 0: exit()
    point_list = list(map(int,input().split()))
    print(statistics.pstdev(point_list))

