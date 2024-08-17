N,M = map(int,input().split())
H = list(map(int,input().split()))
count = 0
for hands in H:
    M = M-hands
    if M >= 0:        
        count +=1
    else:
        break
print(count)