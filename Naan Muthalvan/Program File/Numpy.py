import numpy as np
def create_sentiment(rating);
if 
rating==1 or rating==2;
return -1 # negative sentiment 
elif 
rating==4 or rating==5;
return 1 # positive sentiment 
else
return 0 # neutral sentiment
df['Sentiment'] = df['Rating'].apply(create_sentiment)

from sklearn.feature_extraction.text import re def clean_data(review):
no_punc = re.sub(r'[^\w\s]', '', review)
no_digits = ''.join([i for i in no_punc if not i.isdigit()]) 
return(no_digits)


df['Review'] = df['Review'].apply(clean_data) 
df['Review'][0]
