from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.utils import to_categorical
from keras.optimizers import Adam
from sklearn.metrics import accuracy_score, classification_report
import numpy as np


def pre_treatment(data):
    # Convert the list of DataFrames into a 3D Numpy array
    return np.array([df.iloc[:, 1:].values for df in data])


def train_ai(train_data, y_train):
    x_train = pre_treatment(train_data)
    y_train = to_categorical(y_train, num_classes=7)

    # Model architecture
    model = Sequential()
    model.add(LSTM(800, activation='tanh', input_shape=(x_train.shape[1], x_train.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(400, activation='tanh', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(200, activation='tanh', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(100, activation='tanh', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(50, activation='tanh'))
    model.add(Dropout(0.2))
    model.add(Dense(7, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=1, validation_split=0.2)

    return model


def test_ai(model, test_data, y_test):
    x_test = pre_treatment(test_data)

    predictions = model.predict(x_test)
    predictions = np.argmax(predictions, axis=1)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    print("Accuracy:", accuracy * 100, " %")
    print("Classification Report:\n", report)
