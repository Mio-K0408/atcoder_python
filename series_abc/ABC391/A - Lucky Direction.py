D = input()
match D:
    case "N":
        print("S")
    case "S":
        print("N")
    case "E":
        print("W")
    case "W":
        print("E")
    case "NE":
        print("SW")
    case "SW":
        print("NE")
    case "NW":
        print("SE")
    case "SE":
        print("NW")