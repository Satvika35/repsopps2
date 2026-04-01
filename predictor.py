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