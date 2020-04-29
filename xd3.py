import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def amarillo(inp,out):
    height, width,c= inp.shape
    image_data = np.asarray(inp)
    for i in range(height):
        for j in range(width):
            if(inp[i][j][0]<=20 or inp[i][j][1]>=200 or inp[i][j][2]>=200):
                out[i][j][0]=0
                out[i][j][1]=0
                out[i][j][2]=0
    cv.imshow('paisaje',out)

p = cv.imread('paisaje.png')
res = cv.imread('blankp.png')
amarillo(p,res)            
histB = cv.calcHist([p], [0], None, [256], [0, 256])
histG = cv.calcHist([p], [1], None, [256], [0, 256])
histR = cv.calcHist([p], [2], None, [256], [0, 256])
plt.plot(histB, color='blue' )
plt.plot(histG, color='green' )
plt.plot(histR, color='red' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
