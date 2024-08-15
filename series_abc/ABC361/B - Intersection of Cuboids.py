# x1, y1, z1, x2, y2, z2 = map(int, input().split())
# x3, y3, z3, x4, y4, z4 = map(int, input().split())

# def func(l1,r1,l2,r2):
#     if r1 <= l2 or r2 <= l1:
#         return False
#     else:
#         return True
    
# if func(x1,x2,x3,x4) and func(y1,y2,y3,y4) and func(z1,z2,z3,z4):
#     print("Yes")
# else:
#     print("No")

# 解説動画のC++コードをPythonに書き直し
class Point:
    # コンストラクタ
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c


def solve():
    a,b,c,d,e,f = map(int, input().split())
    g,h,i,j,k,l = map(int, input().split())
    l1 = Point(a,b,c)
    r1 = Point(d,e,f)
    l2 = Point(g,h,i)
    r2 = Point(j,k,l)
    if r1.x <= l2.x:return False
    if r2.x <= l1.x:return False
    if r1.y <= l2.y:return False
    if r2.y <= l1.y:return False
    if r1.z <= l2.z:return False
    if r2.z <= l1.z:return False
    return True

if solve(): print("Yes")
else: print("No")