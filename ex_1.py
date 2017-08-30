import numpy as np
	
A01 = np.matrix("0.45 1.3 0.94 1.23; 0 0.83 0.2 2.37; 0.2 0.65 0.4 0.3; 0 0 0 1")
A12 = np.matrix("1 0.2 0.85 2.467; 0.54 1.3 0 0.77; 0.12 0.68 1 0.8; 0 0 0 1")
X2 = np.matrix("2.3; 0; 24.4; 1")
print("A01 = \n", A01)
print("A12 = \n", A12)
print("X2 = \n", X2)
print("X0 = \n",np.matrix(A01*A12*X2))