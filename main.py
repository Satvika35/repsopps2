# main.py

from predictor import predict_questions

def main():
    print(" Question Paper Predictor System\n")
    
    predicted_questions = predict_questions()
    
    print(" Predicted Important Questions:\n")
    
    for i, (question, count) in enumerate(predicted_questions, start=1):
        print(f"{i}. {question} (Repeated {count} times)")

if __name__ == "__main__":
    main()
