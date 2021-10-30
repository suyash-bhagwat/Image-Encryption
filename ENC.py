from PIL import Image
from random import randint
import sys
import numpy
from helper import *

im = Image.open('input/' + sys.argv[1]).convert('LA')
pix = []
pix = im.load()

matrix = []

for i in range(im.size[0]):
	matrix.append([])
	for j in range(im.size[1]):
		PerPixel = pix[i,j]
		matrix[i].append(PerPixel[0])

m = im.size[0]
n = im.size[1]


alpha = 8
#kr for rows
Kr = [randint(0,pow(2,alpha)-1) for i in range(m)]
# kc for columns
Kc = [randint(0,pow(2,alpha)-1) for i in range(n)]
ITER_MAX = 1

print('Vector Kr : ', Kr)
print('Vector Kc : ', Kc)

f = open('keys.txt','w+')
f.write('Vector Kr : \n')
for a in Kr:
	f.write(str(a) + '\n')
f.write('Vector Kc : \n')
for a in Kc:
	f.write(str(a) + '\n')
f.write('ITER_MAX : \n')
f.write(str(ITER_MAX) + '\n')


for iterations in range(ITER_MAX):
	# For each row
	for i in range(m):
		totalsum = 0
		totalsum = sum(matrix[i])
		summodulas = totalsum % 2
		if(summodulas == 0):
			matrix[i] = numpy.roll(matrix[i],Kr[i])
		else:
			matrix[i] = numpy.roll(matrix[i],-Kr[i])
			
	#For each column
	for i in range(n):
		totalsum = 0
		for j in range(m):
			totalsum += matrix[j][i]
		summodulas = totalsum % 2
		if(summodulas == 0):
			upshift(matrix,i,Kc[i])
		else:
			downshift(matrix,i,Kc[i])
	# For each row
	for i in range(m):
		for j in range(n):
			if(i%2==1):
				matrix[i][j] = matrix[i][j] ^ Kc[j]
			else:
				matrix[i][j] = matrix[i][j] ^ rotate180(Kc[j])

	# For each column
	for j in range(n):
		for i in range(m):
			if(j%2==0):
				matrix[i][j] = matrix[i][j] ^ Kr[i]
			else:
				matrix[i][j] = matrix[i][j] ^ rotate180(Kr[i])

for i in range(m):
	for j in range(n):
		pix[i,j] = (matrix[i][j],)

im.save('encrypted_images/' + sys.argv[1])
print("Image Encrypted Successfully........")
