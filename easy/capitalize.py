import os

# Complete the solve function below.
def solve(s):
    inp = s.split(" ")
    
    for i in range(len(inp)):
        inp[i] = inp[i].capitalize()
   
    return ' '.join(inp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()