# Practical 13: Confusion Matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def generate_confusion_matrix():
    # Imagine a doctor testing 10 patients for a disease (1 = Sick, 0 = Healthy)
    
    # The ACTUAL truth
    actual_answers = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    
    # What our AI MODEL predicted
    predicted_answers = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    # Notice: It made two mistakes! 
    # - It guessed 1 when it was actually 0
    # - It guessed 0 when it was actually 1

    # Generate the matrix
    cm = confusion_matrix(actual_answers, predicted_answers)
    
    # Display it visually
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Healthy', 'Sick'])
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix for Disease Prediction")
    
    plt.savefig("confusion_matrix.png")
    print("Confusion Matrix saved to 'confusion_matrix.png'!")

if __name__ == "__main__":
    generate_confusion_matrix()
