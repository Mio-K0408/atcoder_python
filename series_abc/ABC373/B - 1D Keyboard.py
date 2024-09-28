S = input()
count = 0
tmp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for index,target in enumerate(tmp):
    if index == 0:
        pass
    else:
        before = S.find(tmp[index-1])
        current = S.find(target)        
        count += abs(before-current)
        # print('{}:{}:{}'.format(target,str(abs(before-current)),str(count)))


print(count)