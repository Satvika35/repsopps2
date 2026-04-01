# utils.py

from collections import Counter

def count_frequency(questions):
    # Count how many times each question appears
    frequency = Counter(questions)
    return frequency

def get_top_questions(frequency, top_n=3):
    # Get most common questions
    return frequency.most_common(top_n)
