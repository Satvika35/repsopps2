# predictor.py

from data_loader import load_data
from utils import count_frequency, get_top_questions

def predict_questions():
    # Load data
    questions = load_data()
    
    # Count frequency
    frequency = count_frequency(questions)
    
    # Get top predicted questions
    predicted = get_top_questions(frequency)
    
    return predicted

if __name__ == "__main__":
    result = predict_questions()
    print("Predicted Questions:")
    for question, count in result:
        print(f"{question} ({count} times)")
