# Practical 12: Multiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

def run_multiple_linear_regression():
    # Example: Predicting House Price based on TWO inputs!
    # Input X: [Bedrooms, Age of House in years]
    X = np.array([
        [3, 10], # 3 beds, 10 years old
        [4, 5],  # 4 beds, 5 years old
        [2, 20], # 2 beds, 20 years old
        [5, 2]   # 5 beds, 2 years old
    ])
    
    # Output Y: House Price (in thousands)
    Y = np.array([300, 450, 150, 600])
    
    # Train the Model
    model = LinearRegression()
    model.fit(X, Y)
    
    # PREDICT: What is the price of a house with 4 bedrooms that is 10 years old?
    # We pass it a new 2D array [4, 10]
    future_house = np.array([[4, 10]])
    prediction = model.predict(future_house)
    
    print("--- MULTIPLE LINEAR REGRESSION ---")
    print("Knowledge learned:")
    print(f"Weight for Bedrooms: {model.coef_[0]:.2f} (Price increases this much per room)")
    print(f"Weight for House Age: {model.coef_[1]:.2f} (Price decreases this much per year)\n")
    
    print(f"Predicted Price for 4 Bed, 10 Year Old House: ${prediction[0]:.2f}k")
    
if __name__ == "__main__":
    run_multiple_linear_regression()
