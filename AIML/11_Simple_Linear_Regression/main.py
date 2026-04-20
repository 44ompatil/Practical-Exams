# Practical 11: Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def run_simple_linear_regression():
    # 1. Fake data: Years of Experience vs Salary (in thousands)
    # X must be a 2D array for scikit-learn
    X = np.array([[1], [2], [3], [4], [5]]) 
    Y = np.array([40, 50, 60, 70, 80])
    
    # 2. Let's create and train the model!
    model = LinearRegression()
    model.fit(X, Y)
    
    # 3. Predict the future! If someone has 6 years of experience, what's the salary?
    prediction = model.predict([[6]])
    print(f"Prediction for 6 years of experience: ${prediction[0]:.2f}k")
    
    # 4. Plot the "Line of Best Fit"
    plt.scatter(X, Y, color='blue', label='Actual Data')
    plt.plot(X, model.predict(X), color='red', label='Line of Best Fit')
    plt.scatter([[6]], prediction, color='green', marker='x', s=100, label='Prediction')
    
    plt.title("Years of Experience vs Salary")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary (in thousands)")
    plt.legend()
    
    plt.savefig("simple_regression.png")
    print("Chart saved to 'simple_regression.png'")

if __name__ == "__main__":
    run_simple_linear_regression()
