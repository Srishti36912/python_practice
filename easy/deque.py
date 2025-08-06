from collections import deque

N = int(input())
d = deque()

for i in range(N):
    operation = input().split()
    if operation[0] == 'append':
        d.append(int(operation[1]))
    if operation[0] == 'pop':
        d.pop()
    if operation[0] == 'popleft':
        d.popleft()
    if operation[0] == 'appendleft':
        d.appendleft(int(operation[1]))
 
for i in d:       
    print(i, end=' ')