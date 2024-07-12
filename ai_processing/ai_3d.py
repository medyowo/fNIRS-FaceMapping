from keras import Input
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np


def pre_treatment(data):
    # Convert the list of DataFrames into a 3D Numpy array
    return np.array([df.iloc[:, 1:].values for df in data])


def train_ai(train_data, y_train):
    x_train = pre_treatment(train_data)

    # Model architecture
    model = Sequential()
    shape = Input((x_train.shape[1], x_train.shape[2]))
    model.add(LSTM(50)(shape))
    model.add(Dense(1, activation='relu'))

    model.compile(loss='mse', optimizer='adam')
    model.fit(x_train, y_train, batch_size=128, epochs=20)

    return model


def test_ai(model, test_data, y_test):
    x_test = pre_treatment(test_data)
