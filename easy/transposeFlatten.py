import numpy

N, M = map(int, input().split())


data = [input().split() for i in range(N)]
    
arr = numpy.array(data, int)

print(numpy.transpose(arr))
print(arr.flatten())