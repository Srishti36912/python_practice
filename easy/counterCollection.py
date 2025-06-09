from collections import Counter

total=0
x=int(input())

shoe_size=list(map(int,input().split()))

n=int(input())

c=Counter(shoe_size)

for i in range(n):
    size,price=map(int,input().split())
    if c[size]!=0:
        total+=price
        c[size]-=1
        
print(total)