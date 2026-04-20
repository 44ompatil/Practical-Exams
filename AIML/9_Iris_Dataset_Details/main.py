# Practical 9: Load Iris Dataset
import pandas as pd
from sklearn.datasets import load_iris

def load_and_display_iris():
    # 1. Load the famous dataset from scikit-learn
    iris = load_iris()
    
    # 2. Convert it into a Pandas DataFrame so it looks like an Excel sheet
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    
    # Add the target answers (the species of the flower)
    df['species_number'] = iris.target
    
    print("--- IRIS DATASET DETAILS ---")
    print(f"Total number of flowers measured (Rows): {df.shape[0]}")
    print(f"Total number of measurements per flower (Columns): {df.shape[1] - 1}\n")
    
    print("--- FIRST 5 ROWS ---")
    print(df.head())
    print("\n")
    
    print("--- STATISTICAL DESCRIPTION ---")
    # This gives us the average, max, and min values for flower petals!
    print(df.describe())

if __name__ == "__main__":
    load_and_display_iris()
