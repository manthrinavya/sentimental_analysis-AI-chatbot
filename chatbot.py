import pandas as pd
from difflib import get_close_matches
from sentiment import analyze_sentiment

# Load dataset
data = pd.read_csv("data/sample_data.csv")

def chatbot(user_input):

    sentiment = analyze_sentiment(user_input)

    questions = data["question"].tolist()

    match = get_close_matches(user_input, questions, n=1, cutoff=0.4)

    if match:
        answer = data.loc[data["question"] == match[0], "answer"].values[0]
    else:
        answer = "Sorry, I couldn't find an answer to your question."

    return answer, sentiment