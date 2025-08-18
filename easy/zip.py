elements = input().split(' ')
N = int(elements[0])
X = int(elements[1])
li = []

for i in range(X):
    li.append(list(map(float, input().split(' '))))

for i in zip(*li):
    print(f'{(sum(i) / len(i)):.1f}')