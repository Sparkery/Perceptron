#Spastoric
#April 25, 2013
#Perceptron With Finite Differences Method

from math import exp

epoch = 10000

def sigmoid(w, x, z): #Sigmoid function
  y = w + w1*x + w2*z
	sig = 1 / (1 + exp(-y))
	return sig

#Demonstrating the logical OR weights

w0 = -8
w1 = 4
w2 = 1 #Random initialization of weights

test = [(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)] #Test data

for A in range(epoch):
	error = 0
	for (x, z, p) in test:
		error += 0.5*(p - sigmoid(w0, x, z))**2
	print(error)
	dw = 0.01 #Finite difference
	error1 = 0
	error2 = 0
	error3 = 0
	for (x, z, p) in test:
		error1 += 0.5*(p - sigmoid(w0 + dw, x, z))**2 #Estimating derivatives
		error2 += 0.5*(p - sigmoid(w0, x + dw, z))**2
		error3 += 0.5*(p - sigmoid(w0, x, z + dw))**2
	w0 += (error - error1) #Changing weights to reduce error
	w1 += (error - error2)
	w2 += (error - error3)

error = 0 #Final calculation of error
for (x, z, p) in test:
	error += 0.5*(p - sigmoid(w0, x, z))**2

print(10000, error, w0, w1, w2)
