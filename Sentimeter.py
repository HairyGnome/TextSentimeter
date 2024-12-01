import os
import numpy
import tensorflow as tf
from keras.utils import pad_sequences

from DataSerializer import DataSerializer

batch_size = 256
epochs = 5


def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=(None,)),
        tf.keras.layers.Embedding(input_dim=256, output_dim=64),
        tf.keras.layers.LSTM(units=64),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(units=64, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(units=32, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(units=16, activation='relu'),
        tf.keras.layers.Dense(units=5, activation='softmax')
    ])
    return model

if __name__ == '__main__':
    model = create_model()
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss=tf.keras.losses.categorical_crossentropy, metrics=['accuracy'])

    serializer = DataSerializer()
    data, labels = serializer.load('/data/training')
    eval_data, eval_labels = serializer.load('/data/evaluation')


    MAX_LENGTH = 100
    data = pad_sequences(data, padding='post', maxlen=MAX_LENGTH)
    eval_data = pad_sequences(eval_data, padding='post', maxlen=MAX_LENGTH)

    data = numpy.array(data)
    eval_data = numpy.array(eval_data)
    labels = numpy.array(labels)
    eval_labels = numpy.array(eval_labels)

    try:
        model.fit(data, labels, batch_size=batch_size, epochs=epochs, validation_split=0.1)
        test_loss, test_accuracy = model.evaluate(eval_data, eval_labels)
    except KeyboardInterrupt:
        pass
    finally:
        save_input = input('Save model? (Y/N) ')
        save_input = save_input.capitalize()
        if save_input == 'Y':
            model.save(f'{os.curdir}/models/{test_accuracy}', overwrite=False)