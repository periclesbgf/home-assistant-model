import sounddevice as sd
import scipy.io.wavfile as wav
import random
import string
import os
import time

tamanho_string = 10
EDEN_PATH = 'audios/eden/'
ON_PATH = 'audios/on/'
OFF_PATH = 'audios/off/'
MARVIN_PATH = 'audios/marvin/'
LIGUE_PATH = 'audios/ligue/'
DESLIGUE_PATH = 'audios/desligue/'
BACKGROUND_PATH = 'audios/background/'

# Configurações para a gravação de áudio
samplerate = 16000  # Taxa de amostragem (16kHz)
duration = 1  # Duração da gravação em segundos

def verify_dir():
    if os.path.exists('audios/eden/') and os.path.isdir('audios/eden/'):
        return 1
    return 0

# Função para gravar áudio
def gravar_audio(samplerate, duration):
    time.sleep(0.2)
    print("Gravando áudio...")
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Aguarda até que a gravação seja concluída
    return audio_data

def iniciar_gravacao(path):
    # Grava o áudio
    audio_data = gravar_audio(samplerate, duration)

    # Caminho para salvar o arquivo .wav
    string_aleatoria = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho_string))
    caminho_arquivo = path + string_aleatoria + ".wav"

    # Salva o áudio em um arquivo .wav
    wav.write(caminho_arquivo, samplerate, audio_data)

    print(f"Áudio gravado e salvo em '{caminho_arquivo}'\n")

def background_recording():
    while True:
        iniciar_gravacao(BACKGROUND_PATH)

if __name__ == "__main__":
    if verify_dir() == 0:
        os.mkdir('./audios')
        os.mkdir('./audios/eden')
        os.mkdir('./audios/on')
        os.mkdir('./audios/off')
        os.mkdir('./audios/marvin')
        os.mkdir('./audios/background')

    while True:
        print('QUANDO PRESSIONAR 1 ou 2 ou 3 ou 4 FALE IMEDIATAMENTE NO MICROFONE\n5 Gravando infinito')
        print('1 - Eden\n2 - On\n3 - Off\n4 - Marvin\n5 - Background recording')
        op = input()
        op = int(op)

        if (op == 1):
            iniciar_gravacao(EDEN_PATH)
        elif (op == 2):
            iniciar_gravacao(ON_PATH)
        elif (op == 3):
            iniciar_gravacao(OFF_PATH)
        elif (op == 4):
            iniciar_gravacao(MARVIN_PATH)
        elif (op == 5):
            background_recording()

