pip install -q textblob
from textblob import TextBlob data = ["I love you", "I hate you"] for text in data;
blob = TextBlob(text) print(blob.sentiment)
