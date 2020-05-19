import pandas as pd
import numpy as np 
from keras.preprocessing.sequence import pad_sequences
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
	text = text.lower()
	# use regex to clean up html tags
	cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	text = re.sub(cleanr, '', text)
	text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
	return text

def classifyjob(resume, jobcategories, tokenizer, model):
	text = pd.DataFrame({"text" : resume}, index=[1])
	text['cleaned'] = text['text'].apply(clean_text)
	text_sequences = tokenizer.texts_to_sequences(text['cleaned'].values)
	text_sequences = pad_sequences(text_sequences, maxlen=250)
	pred = model.predict(text_sequences)
	# returns the job 5 titles to search on LinkedIn
	return jobcategories[np.argmax(pred)]
