import re

S = input()
k = input()

m = list(re.finditer(rf"(?={k})", S))

if m == []:
    print((-1, -1))

for i in m:
    print(tuple((i.start(), i.start() + len(k)-1)))