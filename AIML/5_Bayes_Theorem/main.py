# Practical 5: Bayes' Theorem

def bayes_theorem(p_disease, p_positive_given_disease, p_false_positive):
    """
    Calculates probability of actually having the disease if tested positive.
    """
    print(f"Base Probability of having the disease (P(A)): {p_disease * 100}%")
    print(f"Probability of testing positive if you have it (P(B|A)): {p_positive_given_disease * 100}%")
    print(f"Probability of testing positive if you DONT have it (False Alarm): {p_false_positive * 100}%\n")

    # Probability of actually having it AND testing positive
    p_true_positive = p_disease * p_positive_given_disease
    
    # Probability of NOT having it (1 - p_disease) but getting a false positive
    p_false_alarm_total = (1 - p_disease) * p_false_positive
    
    # Total probability of getting a positive test result (True Positive + False Positive)
    p_total_positive = p_true_positive + p_false_alarm_total
    
    # Bayes Theorem: P(A|B) = P(B|A) * P(A) / P(B)
    # The chance you have it GIVEN a positive test = (True Positives) / (All Positives)
    probability = (p_true_positive / p_total_positive) * 100
    
    return probability

if __name__ == "__main__":
    # Example: A rare disease
    p_disease = 0.01 # 1% of population has it
    p_positive_given_disease = 0.99 # 99% of sick people test positive
    p_false_positive = 0.05 # 5% of healthy people test positive accidentally
    
    result = bayes_theorem(p_disease, p_positive_given_disease, p_false_positive)
    
    print(f"If you test positive, your actual chance of having the disease is ONLY: {result:.2f}%")
    print("Why? Because it's a rare disease, the false alarms outnumber the truly sick people!")
