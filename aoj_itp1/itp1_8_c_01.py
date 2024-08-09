import string
import sys

ALL = sys.stdin.read()
list1 = list(string.ascii_lowercase)
list2 = [0]*26
str_count = dict(zip(list1,list2))

for s in ALL:
    a = s.lower()
    if a:
        for tmp in a:
            if tmp.isalpha():
                str_count[tmp]+=1
    else:
        break

for k,v in str_count.items():
    print("{} : {}".format(k,v))