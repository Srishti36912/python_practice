t = int(input())
l = [input().split() for i in range(t)]
    
for i in l:
    try:
        print(int(i[0]) // int(i[1]))
    
    except Exception as e:
        print("Error Code:", e)