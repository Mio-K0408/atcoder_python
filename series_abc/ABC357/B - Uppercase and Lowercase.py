S = input()
upper_count = sum(a.isupper()for a in S)
if upper_count > len(S) - upper_count:
    print(S.upper())
else:
    print(S.lower())