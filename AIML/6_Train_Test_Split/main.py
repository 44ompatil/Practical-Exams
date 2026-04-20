# Practical 6: Splitting Dataset into Train and Test Sets
import pandas as pd
from sklearn.model_selection import train_test_split

def demonstrate_split():
    # 1. Let's create a fake list of 10 students and their exam scores
    data = {
        'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Hours_Studied': [2, 3, 1, 5, 4, 6, 8, 7, 9, 10],
        'Exam_Passed': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']
    }
    
    df = pd.DataFrame(data)
    print("--- ORIGINAL ENTIRE DATASET (10 Students) ---")
    print(df)
    print("\n")
    
    # 2. We separate the Features (X) from the Target Answer (Y)
    X = df[['Student_ID', 'Hours_Studied']]
    Y = df['Exam_Passed']
    
    # 3. We use scikit-learn to split it! 80% for studying, 20% for the exam.
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    print("--- TRAINING SET (8 Students we learn from) ---")
    print(X_train)
    print("\n")
    
    print("--- TESTING SET (2 Students we use to quiz the AI) ---")
    print(X_test)

if __name__ == "__main__":
    demonstrate_split()
