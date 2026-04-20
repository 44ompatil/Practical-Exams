# Practical 7: Decision Tree
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

def build_decision_tree():
    # 1. Let's make some simple data about whether we should play Golf outside
    data = {
        'Weather_Is_Sunny': [1, 1, 0, 0, 1, 0], # 1=Yes, 0=No
        'Is_Windy':         [0, 1, 0, 1, 0, 1], # 1=Yes, 0=No
        'Play_Golf':        [1, 0, 1, 0, 1, 0]  # 1=Play, 0=Stay Home
    }
    df = pd.DataFrame(data)
    
    X = df[['Weather_Is_Sunny', 'Is_Windy']]
    Y = df['Play_Golf']
    
    # 2. Build the Model
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(X, Y)
    
    # 3. Draw the tree!
    plt.figure(figsize=(10, 6))
    plot_tree(clf, feature_names=['Sunny', 'Windy'], class_names=['Stay Home', 'Play'], filled=True)
    plt.title("Decision Tree: Should we play Golf?")
    
    # Save to file so we can view it
    plt.savefig("decision_tree_output.png")
    print("Decision Tree drawn and saved to 'decision_tree_output.png'. Check the folder!")

if __name__ == "__main__":
    build_decision_tree()
