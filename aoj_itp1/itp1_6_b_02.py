n = int(input())
main_list = []
for i in range(1,14):
    main_list.append(i)

input_dict = {"S":[],"H":[],"C":[],"D":[]}
for i in range(n):
    mark,num = input().split()
    tmp_list = input_dict[mark]
    tmp_list.append(int(num))
    input_dict[mark] = tmp_list

for key,value_list in input_dict.items():
    dif_list = set(main_list) ^ set(value_list)
    for item in dif_list:
        print("{} {}".format(key,item))
    


    
