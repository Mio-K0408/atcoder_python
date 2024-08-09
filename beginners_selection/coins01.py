a = int(input()) #500円玉
b = int(input()) #100円玉
c = int(input()) #50円玉
x = int(input()) #合計金額
count = 0

for i_a in range(0,a+1):
    for i_b in range(0,b+1):
        for i_c in range(0,c+1):
            total = 500*i_a + 100*i_b + 50*i_c
            if total == x:
                count+=1

print(count)

