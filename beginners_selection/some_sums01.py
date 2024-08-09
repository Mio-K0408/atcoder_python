n, a, b = map(int, input().split())
total = 0
for num in range(1,n+1):    
    tmp_total = sum(list(map(int,str(num))))    
    if a <= tmp_total <= b:
        total += num

print(total)