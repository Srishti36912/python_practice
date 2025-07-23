import numpy

N, M = map(int, input().split())

val = [list(map(int, input().split())) for i in range(N)]

array = numpy.array(val)

min = numpy.min(array, axis=1)

print(numpy.max(min))