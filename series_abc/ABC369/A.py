"""
    答案1
"""
A,B = map(int,input().split())
tmp = B-A
if tmp == 0:
    print(1)
elif tmp % 2 ==0:
    print(3)
else:
    print(2)