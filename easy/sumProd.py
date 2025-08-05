import numpy as np

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(N)]

print(np.prod(np.sum(arr, axis=0)))