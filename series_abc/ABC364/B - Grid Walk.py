H,W = map(int, input().split())
Si,Sj = map(int, input().split())
C = []
for i in range(H):
    C.append(input())
X = input()
for now in X:
    match now:
        case "L":
            if Sj != 1 and C[Si-1][Sj-2] == ".":
                Sj -=1
        case "R":
            if Sj != W and C[Si-1][Sj] == ".":
                Sj += 1
        case "U":
            if Si != 1 and C[Si-2][Sj-1] == ".":
                Si -= 1
        case "D":
            if Si != W and C[Si][Sj-1] == ".":
                Si += 1

print("{} {}".format(Si,Sj))