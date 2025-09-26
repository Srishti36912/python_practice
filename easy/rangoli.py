def print_rangoli(size):
    # your code goes here
    n = size
    letter = 96 + n 
    max_len = 4 * n - 3
    str = []
    
    for i in range(n):
        s = []
        for j in range(letter, letter-i-1, -1):
            s.append(chr(j))
        for k in range(letter-i+1, letter+1):
            s.append(chr(k))
        str.append("-".join(s))
        
    for string in str:
        print(string.center(max_len, '-'))
    str.reverse()
    for string in str[1:]:
        print(string.center(max_len, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)