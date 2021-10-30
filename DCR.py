from PIL import Image
from random import randint
import numpy
import sys
from helper import *

im = Image.open('encrypted_images/' + sys.argv[1])
pix = im.load()

matrix = []

for i in range(im.size[0]):
	matrix.append([])
	for j in range(im.size[1]):
		PerPixel = pix[i,j]
		matrix[i].append(PerPixel[0])

m = im.size[0]
n = im.size[1]

Kr = []
Kc = []

print('Enter value of Kr')

for i in range(m):
	Kr.append(int(input()))

print('Enter value of Kc')
for i in range(n):
	Kc.append(int(input()))

print('Enter value of ITER_MAX')
ITER_MAX = int(input())

for iterations in range(ITER_MAX):
    # For each column
    for j in range(n):
        for i in range(m):
            if(j%2==0):
                matrix[i][j] = matrix[i][j] ^ Kr[i]
            else:
            	matrix[i][j] = matrix[i][j] ^ rotate180(Kr[i])
    #For each row
    for i in range(m):
        for j in range(n):
            if(i%2==1):
                matrix[i][j] = matrix[i][j] ^ Kc[j]
            else:
                matrix[i][j] = matrix[i][j] ^ rotate180(Kc[j])

    #For each column
    for i in range(n):
        totalsum = 0
        for j in range(m):
            totalsum += matrix[j][i]
        summodulas = totalsum % 2
        if(summodulas == 0):
            downshift(matrix,i,Kc[i])
        else:
            upshift(matrix,i,Kc[i])

    # For each row
    for i in range(m):
#        totalsum = 0
        totalsum = sum(matrix[i])
        summodulas = totalsum % 2
        if(summodulas == 0):
            matrix[i] = numpy.roll(matrix[i],-Kr[i])
        else:
            matrix[i] = numpy.roll(matrix[i],Kr[i])

for i in range(m):
    for j in range(n):
        pix[i,j] = (matrix[i][j],)


im.save('decrypted_images/' + sys.argv[1])
print("Image Decrypted Successfully........")