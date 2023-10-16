import numpy as np
from tensorflow.keras import models
from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

# !! Modify this in the correct order
commands = ['_background_noise_', 'background', 'backward', 'eden', 'marvin','off', 'on']

loaded_model = models.load_model("../saved")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)

if __name__ == "__main__":
    while True:
        predict_mic()
