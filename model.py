import math
import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.001, num_iterations=10000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def initialize_parameters(self, num_features):
        self.weights = [0] * num_features
        self.bias = 0

    def dot_product(self, features, weights):
        return sum(f * w for f, w in zip(features, weights))

    def train(self, X, y):
        m = len(X)  # Number of training examples
        num_features = len(X[0])  # Number of features in the training data

        self.initialize_parameters(num_features)

        for _ in range(self.num_iterations):
            # Forward pass
            predictions = [self.sigmoid(self.dot_product(x[:-1], self.weights) + self.bias) for x in X]

            # Backward pass
            dw = [sum((pred - label) * feature for pred, label, feature in zip(predictions, y, feature_set[:-1])) for feature_set in X]
            db = sum(pred - label for pred, label in zip(predictions, y))

            # Update parameters
            self.weights = [w - (self.learning_rate * grad) / m for w, grad in zip(self.weights, dw)]
            self.bias -= (self.learning_rate * db) / m

    # Function to predict the output
    def predict(self, X, y):
        predictions = [round(self.sigmoid(self.dot_product(x[:-1], self.weights) + self.bias)) for x in X]
        # Calculate accuracy
        accuracy = sum(pred == label for pred, label in zip(predictions, y)) / len(y) * 100
        return accuracy, predictions
