from collections import Counter

k = int(input())
Counted = Counter(list(map(int, input().split())))

for k,v in Counted.items():
    if v == 1:
        print(k)