from textblob import TextBlob

def predict(x):
    analysis = TextBlob(x)
    polarity = analysis.sentiment[0]
    return polarity
