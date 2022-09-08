import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import RNN
from keras.utils import np_utils
text=(open("DataSets\Mortalk Instrument (series).txt").read())
text=text.lower()
characters = sorted(list(set(text)))

# DK WTH IS HAPPENNING START =======================>
n_to_char = {n:char for n, char in enumerate(characters)}
char_to_n = {char:n for n, char in enumerate(characters)}
# DK WTH IS HAPPENING END ==========================>

training_array = []
target_array = []
length = len(text)

# DK WTH IS HAPPENNING START =======================>
seq_length = 100
for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label =text[i + seq_length]
    training_array.append([char_to_n[char] for char in sequence])
    target_array.append(char_to_n[label])
training_array_modified = np.reshape(training_array, (len(training_array), seq_length, 1))
training_array_modified = training_array_modified / float(len(characters))
target_array_modified = np_utils.to_categorical(target_array)
# DK WTH IS HAPPENING END ==========================>

# DK WTH IS HAPPENNING START =======================>
model = Sequential()
model.add(LSTM(400, input_shape=(training_array_modified.shape[1], training_array_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400))
model.add(Dropout(0.2))
model.add(Dense(target_array_modified.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
# DK WTH IS HAPPENING END ==========================>

string_mapped = training_array[99]
# generating characters
for i in range(seq_length):
    x = np.reshape(string_mapped,(1,len(string_mapped), 1))
    x = x / float(len(characters))
    pred_index = np.argmax(model.predict(x, verbose=0))
    seq = [n_to_char[value] for value in string_mapped]
    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]

