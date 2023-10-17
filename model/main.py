import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer
import pathlib

DATA_PATH = '../data/google'

data_dir = pathlib.Path(DATA_PATH)
# Extraindo do diretório data o nome dos arquivos que significam as palavras disponíveis
commands = np.array(tf.io.gfile.listdir(str(data_dir)))
commands = commands[(commands != 'README.md') & (commands != '.DS_Store') & (commands != '.txt') & (commands != 'testing_list.txt') & (commands != 'validation_list.txt') & (commands != 'LICENSE')]
train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
    directory=data_dir,
    batch_size=64,
    validation_split=0.2,
    seed=0,
    output_sequence_length=16000,
    subset='both')

label_names = np.array(train_ds.class_names)

commands = label_names

print('Commands:', commands)

loaded_model = models.load_model("saved")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted:", command)

if __name__ == "__main__":
    while True:
        predict_mic()
