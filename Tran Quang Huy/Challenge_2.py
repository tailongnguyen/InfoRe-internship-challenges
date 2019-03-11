# -*- coding: utf-8 -*-
"""IntentClassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18XbwMlRbtF3mfneKiI33kiOkv4OeaUvD
"""

from google.colab import drive 
drive.mount('/content/mydrive/')
import sys
sys.path.append("/content/mydrive/My Drive/app/")

import pandas as pd
import numpy as np
import re
import tensorflow as tf
import nltk
import functools
from nltk.tokenize import word_tokenize
from keras.models import Sequential
from keras import layers
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from keras.layers import Dense, Activation, Dropout, Embedding, Bidirectional, LSTM, GRU
from keras.preprocessing import text, sequence
from keras import utils
from keras.callbacks import ModelCheckpoint
from keras.models import load_model

nltk.download('punkt')

# set data path
filepath_dict = {'SearchCreativeWork': '/content/mydrive/My Drive/app/intent-train-data/SearchCreativeWork.txt',
                 'GetWeather': '/content/mydrive/My Drive/app/intent-train-data/GetWeather.txt',
                 'BookRestaurant': '/content/mydrive/My Drive/app/intent-train-data/BookRestaurant.txt',
                 'PlayMusic': '/content/mydrive/My Drive/app/intent-train-data/PlayMusic.txt',
                 'AddToPlaylist': '/content/mydrive/My Drive/app/intent-train-data/AddToPlaylist.txt',
                 'RateBook': '/content/mydrive/My Drive/app/intent-train-data/RateBook.txt', 
                 'SearchScreeningEvent': '/content/mydrive/My Drive/app/intent-train-data/SearchScreeningEvent.txt'}

# get data from data path
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    
    # if source == 'SearchCreativeWork':
    #   df['label'] = 0
    # elif source == 'GetWeather':
    #   df['label'] = 1
    # elif source == 'BookRestaurant':
    #   df['label'] = 2
    # elif source == 'PlayMusic':
    #   df['label'] = 3
    # elif source == 'AddToPlaylist':
    #   df['label'] = 4
    # elif source == 'RateBook':
    #   df['label'] = 5
    # elif source == 'SearchScreeningEvent':
    #   df['label'] = 6

    
    df_list.append(df)

# get name of 7 class 
df = pd.concat(df_list)
unique_intent = list(set(df['source']))
#print(set(df['label']))

# function return onehot 
def one_hot(encode):
  o = OneHotEncoder(sparse = False)
  return(o.fit_transform(encode))

# return maximum length of word
def max_length(words):
  return(len(max(words, key = len)))

# return tokenizer for store index
def create_tokenizer(words, filters = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
  token = Tokenizer(filters = filters)
  token.fit_on_texts(words)
  return token

def encoding_doc(token, words):
  return(token.texts_to_sequences(words))

def padding_doc(encoded_doc, max_length):
  return(pad_sequences(encoded_doc, maxlen = max_length, padding = "post"))

def create_model(vocab_size, max_length, embedding_matrix, embedding_dim):
  model = Sequential()
  model.add(Embedding(vocab_size, embedding_dim, weights=[embedding_matrix], input_length = max_length, trainable = True))
  model.add(Bidirectional(LSTM(embedding_dim)))
  model.add(Dense(32, activation = "relu"))
  model.add(Dropout(0.25))
  model.add(Dense(7, activation = "softmax"))
  
  return model

# return pretrained embedding matrix from glove
def create_embedding_matrix(filepath, word_index, embedding_dim):
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    with open(filepath) as f:
        for line in f:
            word, *vector = line.split()
            if word in word_index:
                idx = word_index[word] 
                embedding_matrix[idx] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]

    return embedding_matrix

sentences = []
y = []

# add data to array sentences
for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = np.append(sentences, df_source['sentence'].values)
    y = np.append(y, df_source['label'].values)

# find vocab_size and maximum length of word
word_tokenizer = create_tokenizer(sentences)
vocab_size = len(word_tokenizer.word_index) + 1
max_length = max_length(sentences)

print("Vocab Size = %d and Maximum length = %d" % (vocab_size, max_length))
print(word_tokenizer.word_index)

# padding so that all sentences have the same length
encoded_doc = encoding_doc(word_tokenizer, sentences)
padded_doc = padding_doc(encoded_doc, max_length)
print("Shape of padded docs = ",padded_doc.shape)

# define 7 class 
output_tokenizer = {'SearchCreativeWork' : 0, 'GetWeather' : 1, 'BookRestaurant': 2, 'PlayMusic': 3, 'AddToPlaylist': 4, 'RateBook': 5, 'SearchScreeningEvent': 6}
compare_output_tokenizer = {'SearchCreativeWork' : 0, 'GetWeather' : 1, 'BookRestaurant': 2, 'PlayMusic': 3, 'AddToPlaylist': 4, 'RateBook': 5, 'SearchScreeningEvent': 6}
output_tokenizer = create_tokenizer(output_tokenizer)
print(output_tokenizer.word_index)

# one_hot with 7 intent class
encoded_output = encoding_doc(output_tokenizer, df['source'])
encoded_output = np.array(encoded_output).reshape(len(encoded_output), 1)
encoded_output.shape
output_onehot = one_hot(encoded_output)

print(output_onehot.shape)

# split data
train_X, val_X, train_Y, val_Y = train_test_split(padded_doc, output_onehot, shuffle = True, test_size = 0.2)

print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))

# set embedding path, can choose embedding_dim: 50, 100, 200, 300
embedding_dim = 100
embedding_matrix = create_embedding_matrix('/content/mydrive/My Drive/app/glove.6B/glove.6B.100d.txt', word_tokenizer.word_index, embedding_dim)

print(embedding_matrix.shape)

#nonzero_elements = np.count_nonzero(np.count_nonzero(embedding_matrix, axis=1))
#print(nonzero_elements / vocab_size)

model = create_model(vocab_size, max_length, embedding_matrix, embedding_dim)

top3_acc = functools.partial(keras.metrics.top_k_categorical_accuracy, k=3)
top3_acc.__name__ = 'top3_acc'


model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', top3_acc])
model.summary()

filename = '/content/mydrive/My Drive/app/modelfortext.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

hist = model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint])

#loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
#print("Training Accuracy: {:.4f}".format(accuracy))
#loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
#print("Testing Accuracy:  {:.4f}".format(accuracy))
#plot_history(history)

model = load_model("/content/mydrive/My Drive/app/modelfortext.h5")

def predictions(text):
  clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
  test_word = word_tokenize(clean)
  test_word = [w.lower() for w in test_word]
  test_ls = word_tokenizer.texts_to_sequences(test_word)
  print(test_word)
  #Check for unknown words
  if [] in test_ls:
    test_ls = list(filter(None, test_ls))
    
  test_ls = np.array(test_ls).reshape(1, len(test_ls))
 
  x = padding_doc(test_ls, max_length)
  
  pred = model.predict_proba(x)
  
  
  return pred

def get_final_output(pred):
    for index_compare in range(pred.shape[1]):
        if index_compare ==  compare_output_tokenizer.get('SearchCreativeWork'):
            print("{} and {}".format( "SearchCreativeWork has confidence" , pred[0][index_compare]))
        elif index_compare ==  compare_output_tokenizer.get('GetWeather'):
            print("{} and {}".format( "GetWeather has confidence" , pred[0][index_compare]))
        elif index_compare ==  compare_output_tokenizer.get('BookRestaurant'):
            print("{} and {}".format( "BookRestaurant has confidence" , pred[0][index_compare]))
        elif index_compare ==  compare_output_tokenizer.get('PlayMusic'):
            print("{} and {}".format( "PlayMusic has confidence" , pred[0][index_compare]))
        elif index_compare ==  compare_output_tokenizer.get('AddToPlaylist'):
            print("{} and {}".format( "AddToPlaylist has confidence" , pred[0][index_compare]))    
        elif index_compare ==  compare_output_tokenizer.get('RateBook'):
            print("{} and {}".format( "RateBook has confidence" , pred[0][index_compare]))    
        elif index_compare ==  compare_output_tokenizer.get('SearchScreeningEvent'):
            print("{} and {}".format( "SearchScreeningEvent has confidence" , pred[0][index_compare]))

text = " add this track to my epic wall of sound playlist "
pred = predictions(text)
get_final_output(pred)