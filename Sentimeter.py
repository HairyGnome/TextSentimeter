import os

import numpy
import tensorflow as tf
from keras.src.metrics import MeanSquaredError
from keras.src.utils import pad_sequences

from DatabaseParser import DatabaseParser

batch_size = 64
epochs = 200


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=(None,)),
        tf.keras.layers.Embedding(input_dim=1000, output_dim=64),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(units=120, activation='relu'),
        tf.keras.layers.Dense(units=80, activation='relu'),
        tf.keras.layers.Dense(units=40, activation='relu'),
        tf.keras.layers.Dense(units=20, activation='relu'),
        tf.keras.layers.Dense(units=10, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='softmax')
    ])
    return model

if __name__ == '__main__':
    model = create_model()
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.MeanSquaredError(), metrics=['accuracy'])

    db_parser = DatabaseParser(10)
    data, labels, eval_data, eval_labels = db_parser.parse_data(os.curdir + '/data/dataset.csv')

    print(data)

    MAX_LENGTH = 100
    data = pad_sequences(data, padding='post', maxlen=MAX_LENGTH)
    eval_data = pad_sequences(eval_data, padding='post', maxlen=MAX_LENGTH)

    data = numpy.array(data)
    eval_data = numpy.array(eval_data)
    labels = numpy.array(labels)
    eval_labels = numpy.array(eval_labels)

    model.fit(data, labels, batch_size=batch_size, epochs=epochs, validation_split=0.1)
    model.evaluate(eval_data, eval_labels)