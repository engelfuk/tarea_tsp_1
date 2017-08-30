from cinemat import *
import numpy as np

matrix1 = Cinematica()
#datos a)
theta1 = 0
theta2 = 90
theta3 = -90
theta4 = 2
l1 = 1
l2 = 1
l3 = 2
l4 = 1

#Se ingresan los valores de las matrices
A01 = (matrix1.compute_dh(theta1,l3+l4,l1,0))
A12 = (matrix1.compute_dh(theta2,0,l2,0))
A23 = (matrix1.compute_dh(theta3,theta4, 0, 0))
		
#datos b)
theta1 = 0
theta2 = 90
theta3 = -90
theta4 = 2
l1 = 1
l2 = 1
l3 = 2
l4 = 1

#Se ingresan los valores de las matrices
A01 = (matrix1.compute_dh(theta1,l3+l4,l1,0))
A12 = (matrix1.compute_dh(theta2,0,l2,0))
A23 = (matrix1.compute_dh(theta3,theta4, 0, 0))

#Muestra en pantalla los resultados
print("Matrix inciso a)")
print(np.matrix(A01*A12*A23))
print("Coordenadas inciso a) ")
print(matrix1.pos(A01,A12,A23))