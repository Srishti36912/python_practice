def wrapper(f):
    def fun(l):
        # complete the function
        l1 = (i[::-1][0:10][::-1] for i in l)
        l2 = ("+91" +" " +str[0:5] +" " +str[5::] for str in l1)
        return f(l2)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 