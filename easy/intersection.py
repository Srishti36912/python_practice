english = int(input())
eng = set(map(int, input().split()))

french = int(input())
fre = set(map(int, input().split()))
    
print(len(eng.intersection(fre)))
