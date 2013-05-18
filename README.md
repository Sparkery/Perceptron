Perceptron
==========

Engine for a one node neural network

Backpropagation is not used here because many perceptron networks are fast enough without.

Backpropagation uses the Chain Rule for Derivatives to calculate the derivative explicitly instead of estimating it. The formula for this is dE/dw = (z - p)*(z(1 - z)), where p is the expected output, z is the output from the sigmoid function, and z(1 - z) is the derivative of the sigmoid function.
