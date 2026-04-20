# Practical 14: Performance Measures
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def calculate_metrics():
    # 1=Sick, 0=Healthy
    actual    = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    predicted = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    
    # Calculate!
    acc = accuracy_score(actual, predicted)
    prec = precision_score(actual, predicted)
    rec = recall_score(actual, predicted)
    f1 = f1_score(actual, predicted)
    
    print("--- AI REPORT CARD ---")
    print(f"Accuracy:  {acc * 100}%  (Percentage of totally correct guesses)")
    print(f"Precision: {prec * 100}%  (When it guessed 'Sick', how often was it right?)")
    print(f"Recall:    {rec * 100}%  (Out of all actual sick people, how many did it successfully find?)")
    print(f"F1 Score:  {f1 * 100}%  (A balanced average between Precision and Recall)\n")

if __name__ == "__main__":
    calculate_metrics()
