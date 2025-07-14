n = int(input())
s = set(map(int, input().split()))
c = int(input())

for i in range(c):
    f = input().split()
    if f[0] == 'pop':
        s.remove(min(s))
    if f[0] == 'remove':
        s.remove(int(f[1]))
    if f[0] == 'discard':
        s.discard(int(f[1]))
        
print(sum(s))