M = int(input())
el1 = set(map(int, input().split()))
N = int(input())
el2 = set(map(int, input().split()))

for i in sorted(list(el1.symmetric_difference(el2))):
    print(i)