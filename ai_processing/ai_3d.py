from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score, classification_report
import numpy as np


def pre_treatment(data):
    """

    Convert the list of DataFrames into a 3D Numpy array
    データフレームのリストを3DのNumpy配列に変換する

    """
    return np.array([df.iloc[:, 1:].values for df in data])


def train_ai(train_data, y_train):
    """
    
    Create Neural Network and train it with the training database
    ニューラルネットワークを作成し、トレーニングデータベースで訓練する

    """
    # Pretreat data before usage
    # 使用前にデータを前処理する
    x_train = pre_treatment(train_data)
    y_train = to_categorical(y_train, num_classes=7)

    # Model architecture
    # モデルアーキテクチャ
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

    # Model compilation and fitting
    # モデルのコンパイルとフィッティング
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=1, validation_split=0.2)

    return model


def test_ai(model, test_data, y_test):
    """
    
    Test created network with test database
    作成したネットワークをテストデータベースでテストする

    """
    # Pretreat data before usage
    # 使用前にデータを前処理する
    x_test = pre_treatment(test_data)

    # Predict value and keep the highest scored label
    # 値を予測し、最もスコアの高いラベルを保持する
    predictions = model.predict(x_test)
    predictions = np.argmax(predictions, axis=1)

    # Get accuracy and global report
    # 精度と全体レポートを取得する
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    print("Accuracy:", accuracy * 100, " %")
    print("Classification Report:\n", report)
