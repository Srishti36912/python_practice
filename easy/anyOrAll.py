N = int(input())
l = input().split()

print(all(int(i) > 0 for i in l) and any(c == c[::-1] for c in l))