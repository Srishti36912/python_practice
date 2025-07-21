m = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    operation, total_el = input().split()
    new_set = set(map(int, input().split()))
    getattr(A, operation)(new_set)
    
print(sum(A))