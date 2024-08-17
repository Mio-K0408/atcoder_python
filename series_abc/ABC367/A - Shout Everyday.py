A,B,C = map(int,input().split())

if C<=B and C<=A<=B:
    print("Yes")
elif B<=C and (C<=A or A<=B):
    print("Yes")
else:
    print("No")