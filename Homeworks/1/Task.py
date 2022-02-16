import time
import numpy as np

def MatrixInitialization(Rows, Columns):
    matrix = [ [ 1 for i in range(Rows) ] for j in range(Columns) ]
    return matrix

matrixX = MatrixInitialization(500, 500)
matrixY = MatrixInitialization(500, 500)

xNumpy = np.array(matrixX)
yNumpy = np.array(matrixY)

# Loop method
result = MatrixInitialization(500, 500)
startTime = time.time()
for i in range(len(matrixX)):
   for j in range(len(matrixY[0])):
       for k in range(len(matrixY)):
           result[i][j] += matrixX[i][k] * matrixY[k][j]
timeLoop = time.time() - startTime

# Numpy method
startTime = time.time()
results = np.dot(xNumpy, yNumpy)
timeNumpy = time.time() - startTime


print("Time Loop: {:.5f}s ".format(timeLoop))
print("Time Numpy: {:.5f}s ".format(timeNumpy))
