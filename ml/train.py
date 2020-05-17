from keras.models import Sequential, load_model
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
from sklearn.preprocessing import LabelBinarizer

data = pd.read_csv('./Top30.csv')

data = data.reset_index(drop=True)
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    # use regex to clean up html tags
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # remove stopwors from text
    return text
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
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

X = tokenizer.texts_to_sequences(data['Description'].values)
X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
print('Shape of data tensor:', X.shape)

labelbinarizer = LabelBinarizer()
make_encoded_results = labelbinarizer.fit_transform(data['Query'])
df_make_encoded = pd.DataFrame(make_encoded_results, columns=labelbinarizer.classes_)

X_train, X_test, Y_train, Y_test = train_test_split(X,df_make_encoded, test_size = 0.10, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

model = Sequential()
model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(Bidirectional(LSTM(100, dropout=0.2, recurrent_dropout=0.2)))
model.add(Dense(30, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

epochs = 15
batch_size = 64

history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1,
                    callbacks=[EarlyStopping(monitor='val_loss', patience=3, min_delta=0.0001),
                               ModelCheckpoint('./lstm_model.h5', monitor='val_accuracy', verbose=1, 
                                               save_best_only=True, mode='max')])

# model = load_model('model.h5')

# new = 'Excellent communication, collaboration, and planning skills with meticulous attention to detail Ability to successfully organize, prioritize and manage multiple projects under strict deadlines Ability to work weekends from home Ability to write copy that is both emotional and informational You are current with pop culture, music, entertainment news and industry trends Expert understanding of the social ecosystem and how brands should participate in an authentic way Confident in publishing copy and content to mass audiences Experience in music/entertainment specific social media is a major A passion for working in a fast-paced environment with passionate teammates Strategic and creative thinker who can pro-actively problem solve'
# text = pd.DataFrame({"text" : new}, index=[1])
# text['cleaned'] = text['text'].apply(clean_text)
# text_sequences = tokenizer.texts_to_sequences(text['cleaned'].values)
# text_sequences = pad_sequences(text_sequences, maxlen=MAX_SEQUENCE_LENGTH)
# pred = model.predict(text_sequences)
# topic = labelbinarizer.classes_[np.argmax(pred)]