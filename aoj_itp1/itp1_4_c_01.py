# while True:
#     a,b, c = input().split()
#     a,c = int(a),int(c)
#     ans = 0
#     match b:
#         case "+":
#             ans = a + c
#         case "-":
#             ans = a - c
#         case "*":
#             ans = a * c
#         case "/":
#             ans = a // c
#         case "?":
#             exit()
#     print(ans)
while True:
    a,b, c = input().split()
    a,c = int(a),int(c)
    ans = 0
    if b == "+":
        ans = a + c
    if b == "-":
        ans = a - c
    if b == "*":
        ans = a * c
    if b == "/":
        ans = a // c
    if b == "?":
        exit()
    print(ans)
    