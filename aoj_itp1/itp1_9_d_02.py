s=input()
q=int(input())
for i in range(q):
    str=list(input().split())
    ord=str[0]
    if ord=="print":
        a=int(str[1])
        b=int(str[2])
        print(s[a:b+1])
    elif ord=="reverse":
        a=int(str[1])
        b=int(str[2])
        le=s[:a]
        mid=s[a:b+1]
        ri=s[b+1:]
        mid=mid[::-1]
        s=le+mid+ri
    else:
        a=int(str[1])
        b=int(str[2])
        c=str[3]
        le=s[:a]
        mid=c
        ri=s[b+1:]
        s=le+mid+ri
        
