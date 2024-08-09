i = 0
a = int(input())
int_list = list(map(int, input().split()))
while True:
    # check_list = [num%2 == 0 for num in int_list]
    check_list = list(map(lambda x:x % 2 == 0, int_list))    
    if all(check_list):
        i += 1
        #calc_list = [num/2 for num in int_list]
        calc_list = list(map(lambda x:x/2 , int_list))
        #search_list = [num == a for num in calc_list]
        search_list = list(map(lambda x:x == a, calc_list))
        if any(search_list):            
            break
        else:
            int_list = calc_list            
    else:
        break

print(i)