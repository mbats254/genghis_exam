
import numpy as np
arr = np.array([2,3,1,5])

maxElement = np.amax(arr)
print(maxElement)
minElement = np.amin(arr)
all = []
for x in range(minElement, maxElement+1):
  all.append(x)
c = np.setdiff1d(all,arr)

print(c)
