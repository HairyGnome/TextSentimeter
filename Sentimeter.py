import os

import tensorflow as tf
from keras.src.metrics import MeanSquaredError

from DatabaseParser import DatabaseParser

batch_size = 64
epochs = 200


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(),
        tf.keras.layers.Dense(units=120, activation='relu'),
        tf.keras.layers.Dense(units=80, activation='relu'),
        tf.keras.layers.Dense(units=40, activation='relu'),
        tf.keras.layers.Dense(units=20, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='relu'),
        tf.keras.layers.Dense(units=4, activation='relu'),
        tf.keras.layers.Dense(units=4, activation='softmax')
    ])
    return model

if __name__ == '__main__':
    model = create_model()

    db_parser = DatabaseParser(10)
    data, labels = db_parser.parse_data(os.curdir + '/data/dataset.csv')

    model.compile(optimizer=tf.keras.optimizers.Adam, loss=tf.keras.losses.MeanSquaredError, metrics=['accuracy', 'loss'])

    model.fit(data, labels, batch_size=batch_size, epochs=epochs, validation_split=0.1)