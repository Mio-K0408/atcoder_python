from sys import stdin

str_list = list(stdin.readline().split(","))
change_list = []
for target in str_list:
    change_list.append(target.swapcase())

# print(*change_list, sep=',')
print(*['{},'.format(e) for e in change_list], sep='')