"""Modulo de cinemat"""
import numpy as np
from math import *
#from sympy import * #Permite el calculo simbolico

class Cinematica:
	"""
	================================
	Temas Selectos de Programacion
	================================
	It contains compute_dh() funtion, which calculate de transformation using Denavit-Hartemberg (DH) matriz

	"""
	def pos(self,mat1, mat2, mat3):
		"""Shows the  final position [x,y,z] of the final efector in a ROBOT SCARA RRRP 4 GDL"""
		self.mat1 = mat1 
		self.mat2 = mat2
		self.mat3 = mat3
		return [np.matrix(mat1*mat2*mat3)[0,3],np.matrix(mat1*mat2*mat3)[1,3],np.matrix(mat1*mat2*mat3)[2,3]]	

	def compute_dh(self,theta,d,a,alpha):
		""" 
		Ejercicio 2
		Arguments of the function:
			(theta), (distance Zi), (distance Xi), (alpha)
		units in meters and degrees 

		"""
		theta = theta*pi/180
		d = d*pi/180
		a = a*pi/180
		alpha = alpha*pi/180
		
		self.matriz = np.matrix(
			[[cos(theta), -cos(alpha)*sin(theta), sin(alpha)*sin(theta), a*sin(theta)],
			[sin(theta), cos(alpha)*cos(theta), -sin(alpha)*cos(theta), a*sin(theta)],
			[0, sin(alpha),cos(alpha),d],
			[0, 0, 0, 1]])
		return	self.matriz




