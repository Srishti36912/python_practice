t = int(input())

for i in range(t):
    a = int(input())
    el1 = set(map(int, input().split()))
    b = int(input())
    el2 = set(map(int, input().split()))
    if len(el1.difference(el2)) == 0:
        print(True)
    else:
        print(False)