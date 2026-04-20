# Practical 8: K-Means Clustering
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def run_kmeans():
    # 1. We have a bunch of customers' ages and their spending scores
    # Age vs Spending Score
    X = [
        [25, 80], [22, 75], [28, 85], # Young high spenders
        [60, 20], [65, 10], [55, 15], # Old low spenders
        [40, 50], [45, 55], [35, 45]  # Middle age average spenders
    ]
    
    # 2. We want the AI to group them into 3 distinct groups (K=3)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto')
    kmeans.fit(X)
    
    # Get the results
    labels = kmeans.labels_
    
    # 3. Plot them!
    # Extract X (age) and Y (spending) coordinates for plotting 
    ages = [point[0] for point in X]
    spending = [point[1] for point in X]
    
    plt.scatter(ages, spending, c=labels, cmap='rainbow', s=100)
    plt.xlabel("Age")
    plt.ylabel("Spending Score")
    plt.title("Customer Clustering using K-Means")
    
    # Save the output image
    plt.savefig("kmeans_output.png")
    print("K-Means clustering plotted and saved to 'kmeans_output.png'!")

if __name__ == "__main__":
    run_kmeans()
