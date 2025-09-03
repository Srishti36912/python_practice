N = int(input())

for i in range(N):
    el = input()
    
    if len(el) == 10 and (el.startswith('7') or el.startswith('8') or el.startswith('9')) and el.isnumeric():
        print("YES")
    else:
        print("NO")