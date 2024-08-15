R,G,B = map(int,input().split())
C = input()

match C:
    case "Red":
        X = min(G,B)
    case "Green":
        X = min(R,B)
    case "Blue":
        X = min(R,G)

print(X)