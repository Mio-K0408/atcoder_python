S = []
for i in range(12):
    S.append(input())
count = 0
for index,item in enumerate(S):
    if len(item) == index + 1:
        count+=1
    else:
        pass
print(count)