n = int(input())
main_list = []
for i in range(1,14):
    main_list.append(i)
s_list = []
h_list = []
c_list = []
d_list = []
for i in range(n):
    mark,num = input().split()
    if mark == "S":
        s_list.append(int(num))
    elif mark == 'H':
        h_list.append(int(num))
    elif mark == 'C':
        c_list.append(int((num)))
    elif mark == 'D':
        d_list.append(int(num))

if s_list:
    diff_s_list = set(main_list) ^ set(s_list)
    for item in diff_s_list:
        print("S {}".format(item))
if h_list:
    diff_h_list = set(main_list) ^ set(h_list)
    for item in diff_h_list:
        print("H {}".format(item))
if c_list:
    diff_c_list = set(main_list) ^ set(c_list)
    for item in diff_c_list:
        print("C {}".format(item))
if d_list:
    diff_d_list = set(main_list) ^ set(d_list)
    for item in diff_d_list:
        print("D {}".format(item))

    
