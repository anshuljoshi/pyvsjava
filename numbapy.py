
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
print customNumbaSum(1000000000)
end = time.time()
print(end - start)


# Result
# 499999999500000000
# 0.0574541091919


# def customPythonSum(n):
#     temp = 0
#     for i in range(n):
#         temp = temp + i
#     return temp



# start = time.time()
# print customPythonSum(1000000000)
# end = time.time()
# print(end - start)



# Result
# Too much time

