m = int(input())
eng = set(map(int, input().split()))
n = int(input())
fre = set(map(int, input().split()))

print(len(eng | fre))