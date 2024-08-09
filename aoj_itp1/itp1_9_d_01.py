from sys import stdin
input_list,order_list = [],[]
x = 103
for i in range(103):
    input_list.append(stdin.readline())
    if i == 1:
        x = int(input_list[i]) + 1
    elif i == x:
        break


input_str = input_list[0]
count = int(input_list[1])

for i in input_list[2:count+2]:
    order_list.append(i.split())

for target in order_list:
    if target[0] == 'replace':
        a,b,c = int(target[1]),int(target[2]),target[3]
        input_str = input_str[:a] + c + input_str[b+1:]
        # print('replace：'+input_str)
    elif target[0] == 'reverse':
        a,b = int(target[1]),int(target[2])
        tmp_reverse = input_str[a:b+1]
        tmp_before = input_str[:a]
        tmp_after = input_str[b+1:]        
        input_str = tmp_before + tmp_reverse[::-1] + tmp_after
        # print('reverse：'+input_str)
    elif target[0] == 'print':
        a,b = int(target[1]),int(target[2])
        print(input_str[a:b+1])