count = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

alice_score = []
bob_score = []
if count % 2 == 0:
    for index,num in enumerate(num_list):
        if index % 2 != 0:
            alice_score.append(num)
        else:
            bob_score.append(num)
else:
    for index,num in enumerate(num_list):
        if index % 2 == 0:
            alice_score.append(num)
        else:
            bob_score.append(num)

    
score = sum(alice_score) - sum(bob_score)
print(score)
