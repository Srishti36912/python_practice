if __name__ == '__main__':
    N = int(input())
    l = []

    for i in range(N):
        l.append(input().split())
        
    new_l = []
    
    for i in range(len(l)):
        if(l[i][0] == "insert"):
            new_l.insert(int(l[i][1]), int(l[i][2]))
        if(l[i][0] == "print"):
            print(new_l)
        if(l[i][0] == "remove"):
            new_l.remove(int(l[i][1]))
        if(l[i][0] == "append"):
            new_l.append(int(l[i][1]))
        if(l[i][0] == "sort"):
            new_l.sort()
        if(l[i][0] == "pop"):
            new_l.pop()
        if(l[i][0] == "reverse"):
            new_l.reverse()