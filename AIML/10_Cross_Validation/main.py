# Practical 10: Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

def run_cross_validation():
    # Load a standard dataset (e.g. breast cancer prediction dataset)
    data = load_breast_cancer()
    X = data.data
    Y = data.target
    
    # Create our AI model
    model = LogisticRegression(max_iter=10000)
    
    print("Running 5-Fold Cross Validation... Please Wait...")
    # Run Cross Validation using 5 folds
    scores = cross_val_score(model, X, Y, cv=5)
    
    print("\n--- RESULTS ---")
    print("Accuracy of each of the 5 tests:", scores)
    print(f"Average Overall Accuracy: {(scores.mean() * 100):.2f}%")

if __name__ == "__main__":
    run_cross_validation()
