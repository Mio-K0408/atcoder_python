a,b,c = map(int, input().split())
count = 0
while True:
    if c % a == 0:
        count +=1        
    a += 1
    if a > b:
        break

print(count)