import math

N, M = map(int, input().split())

mid = math.floor(N/2);

for i in range(mid):
    print(('.|.'*(i*2+1)).center(M, '-'))

print('WELCOME'.center(M,'-'))

for i in range(mid-1,-1,-1):
    print(('.|.'*(i*2+1)).center(M, '-'))