from itertools import permutations

element = input().split()
S = sorted(element[0])
k = int(element[1])
res = list(permutations(S, k))

for i in res:
    print(''.join(i))