import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    rev = arr[::-1]
    rev_arr = numpy.array(rev, float)
    
    return rev_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)