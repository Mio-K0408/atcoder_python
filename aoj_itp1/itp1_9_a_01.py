w = input()
count = 0
while True:
    t = input()
    if t == 'END_OF_TEXT':
        print(count)
        exit()
    else:
        t_split = t.split()
        for target in t_split:
            if w.upper() == target.upper():
                count += 1