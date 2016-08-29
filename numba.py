
# coding: utf-8


from numba import jit
import numpy as np
import time



@jit
def customNumbaSum(n):
    temp = 0
    for i in range(n):
        temp = temp + i
    return temp



start = time.time()
print customNumbaSum(100000000)
end = time.time()
print(end - start)


# Result
# 4999999950000000
# 0.0726609230042


def customPythonSum(n):
    temp = 0
    for i in range(n):
        temp = temp + i
    return temp



start = time.time()
print customPythonSum(100000000)
end = time.time()
print(end - start)



# Result
# 4999999950000000
# 4.5471470356

