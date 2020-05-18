from keras.models import Sequential
from tensorflow.keras.models import load_model
from keras.layers import Embedding, LSTM, SpatialDropout1D, Bidirectional
from keras.layers.core import Dense
from keras.preprocessing.text import Tokenizer
import pandas as pd
import numpy as np 
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ModelCheckpoint
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))
import pickle

def clean_text(text):
	text = text.lower()
	# use regex to clean up html tags
	cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	text = re.sub(cleanr, '', text)
	text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
	return text

def classifyjob(resume):
	data = pd.read_csv('./Top30.csv')
	data = data.reset_index(drop=True)
	data['Description'] = data['Description'].apply(clean_text)
	data['Query'] = data['Query'].apply(clean_text)
	# The maximum number of words to be used. (most frequent)
	MAX_NB_WORDS = 50000
	# Max number of words in each resume.
	MAX_SEQUENCE_LENGTH = 250
	# Dimension of Embedding.
	EMBEDDING_DIM = 100
	tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
	tokenizer.fit_on_texts(data['Description'].values)

	with open("jobcategories.txt", "rb") as fp:
		jobcategories = pickle.load(fp)

	model = load_model('./lstm_model.h5')

	text = pd.DataFrame({"text" : resume}, index=[1])
	text['cleaned'] = text['text'].apply(clean_text)
	text_sequences = tokenizer.texts_to_sequences(text['cleaned'].values)
	text_sequences = pad_sequences(text_sequences, maxlen=MAX_SEQUENCE_LENGTH)
	pred = model.predict(text_sequences)
	# returns the job 5 titles to search on LinkedIn
	return jobcategories[np.argmax(pred)]
