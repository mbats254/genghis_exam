#!/usr/bin/env python
# coding: utf-8
import numpy as np
# declare an empty array A
A = []
# range from 0 to 100000
N = range(0,100000)
# append each number in the range list to the array A
for x in N:
    if x not in A:
        A.append(x)


# In[ ]:
 print(A)




