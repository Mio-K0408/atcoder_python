S = input()
r_index = 0
m_index = 0
for index,item in enumerate(S):
    if item == "R":r_index=index
    elif item == "M":m_index=index

if r_index < m_index:print("Yes")
else:print("No")