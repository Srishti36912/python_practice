A = set(map(int, input().split()))
N = int(input())
res = []

for i in range(N):
    B = set(map(int, input().split()))
    flag = A.issuperset(B)
    res.append(flag)
    
print(all(res))