class Point:
    # コンストラクタ
    def __init__(self,a,b,c):
        self.u = a
        self.v = b
        self.w = c

N,M = map(int,input().split())
point_list = []
a,b,c = map(int,input().split())
tmp = Point(a,b,c)
point_list.append(tmp)


