import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input layer (2 inputs)
X = np.array([[0.5, 0.8]])

# Weights and bias for hidden layer
W1 = np.array([[0.2, 0.4],
               [0.7, 0.3]])
b1 = np.array([[0.1, 0.1]])

# Weights and bias for output layer
W2 = np.array([[0.6],
               [0.9]])
b2 = np.array([[0.2]])

# -------- Feed Forward Process --------

# Hidden layer calculation
hidden_input = np.dot(X, W1) + b1
hidden_output = sigmoid(hidden_input)

# Output layer calculation
final_input = np.dot(hidden_output, W2) + b2
final_output = sigmoid(final_input)

# Print results
print("Input:", X)
print("Hidden layer output:", hidden_output)
print("Final output:", final_output)