import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model(data_path):
    data = pd.read_csv(data_path, parse_dates=['date'], index_col='date')
    X = data.index.factorize()[0].reshape(-1, 1)
    y = data['value']

    model = Sequential()
    model.add(Dense(10, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')

    model.fit(X, y, epochs=50, batch_size=1, verbose=1)
    model.save('model.h5')
    print("Model trained and saved to model.h5")

if __name__ == "__main__":
    train_model('data/preprocessed_data.csv')