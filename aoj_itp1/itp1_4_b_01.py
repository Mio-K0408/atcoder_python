import math

r = float(input())
area = r * r * math.pi # 円周率
round = 2 * r * math.pi
print("{:.6f} {:.6f}".format(area,round))
