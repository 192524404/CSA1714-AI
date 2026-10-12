import numpy as np

# Sigmoid Activation Function and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Neural Network Weights initialization
np.random.seed(42)
weights_input_hidden = np.random.uniform(size=(2, 2))
weights_hidden_output = np.random.uniform(size=(2, 1))

lr = 0.5  # Learning Rate

# Training loop
for epoch in range(10000):
    # Forward Pass
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    # Backpropagation
    error = y - predicted_output
    d_output = error * sigmoid_derivative(predicted_output)
    
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)

    # Weight updates
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * lr
    weights_input_hidden += X.T.dot(d_hidden) * lr

print("Predictions after training:")
print(np.round(predicted_output, 3))
