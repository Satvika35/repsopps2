# utils.py

from collections import Counter

def count_frequency(questions):
    # Count how many times each question appears
    frequency = Counter(questions)
    return frequency

def get_top_questions(frequency, top_n=3):
    # Get most common questions
    return frequency.most_common(top_n)

if __name__ == "__main__":
    sample_questions = [
        "A", "B", "A", "C", "B", "A"
    ]
    
    freq = count_frequency(sample_questions)
    top = get_top_questions(freq)
    
    print("Frequency:", freq)
    print("Top Questions:", top)

