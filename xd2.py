import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def dead(inp,out):
    height, width = inp.shape
    for i in range(height):
        for j in range(width):
            if(a[i][j]<=190):
                out[i][j]=0
                     
    cv.imshow('muertas',out)
def lives(inp,out):
    height, width = inp.shape
    for i in range(height):
        for j in range(width):
            if(a[i][j]>=190 ):
                out[i][j]=1
           
    cv.imshow('vivas',out)
    
a = cv.imread('celulas1.jpeg',0)
b = cv.imread('celulas2.jpeg',0)
res = cv.imread('blank2.png', 0)
lives(a,res)

            
hist = cv.calcHist([a], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
