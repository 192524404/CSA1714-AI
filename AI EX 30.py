
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Dataset
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([2, 4, 6, 8, 10,
              12, 14, 16, 18, 20])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Display results
print("Predicted Values:", y_pred)
print("Actual Values:", y_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Predict a new value
print("Prediction for X=11:", model.predict([[11]])[0])
