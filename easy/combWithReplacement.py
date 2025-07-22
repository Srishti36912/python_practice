from itertools import combinations_with_replacement

S, r = input().split()
S = sorted(S)
r = int(r)

li = list(combinations_with_replacement(S, r))

for i in li:
    print("".join(i), end= '\n')