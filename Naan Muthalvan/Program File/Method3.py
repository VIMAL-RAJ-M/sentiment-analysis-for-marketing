pip install -q nltk import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer sia = SentimentIntensityAnalyzer()
data = ["I love you", "I hate you"] for text in data:
print(sia.polarity_scores(text))
