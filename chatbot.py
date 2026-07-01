import pandas as pd
from difflib import get_close_matches
from sentiment import analyze_sentiment

# Load dataset
data = pd.read_csv("data/sample_data.csv")

def chatbot(user_input):

    sentiment = analyze_sentiment(user_input)

    questions = data["question"].astype(str).tolist()

    match = get_close_matches(user_input, questions, n=1, cutoff=0.5)

    if match:
        answer = data.loc[data["question"] == match[0], "answer"].values[0]
    else:
        # Default replies if not found in dataset
        user = user_input.lower()

        if "thank" in user:
            answer = "You're welcome! Happy to help."

        elif "hi" in user or "hello" in user:
            answer = "Hello! How can I help you today?"

        elif "who are you" in user:
            answer = "I am the Nullclass Customer Support Chatbot. I can answer your course and support-related questions."

        elif "bye" in user:
            answer = "Goodbye! Have a wonderful day."

        elif "help" in user:
            answer = "Sure! Please tell me what you need help with."

        else:
            answer = "Sorry, I couldn't find this information in my dataset. Please contact Nullclass support for more details."

    return answer, sentiment
