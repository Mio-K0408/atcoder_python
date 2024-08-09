N = int(input())
S = input()
x = 1
count = 0
for target in S:
    if target == 'L':
        if x == 1:
            pass
        else:
            x = x-1
            if x == 3: count +=1
    else:
        if x == 3:
            count +=1
        else:
            x = x+1
            if x == 3: count +=1
print(count)
