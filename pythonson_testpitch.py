# Renvoie une valeur de la hauteur entre -0.5 et 0.5
import librosa
from librosa.beat import tempo
from numpy import lib # Librairie d'analyse de son
from pydub import AudioSegment# Librairie de modification de son
from os import listdir
from os.path import isfile, join
import wave
import numpy as np
def create_chunk(audio_file, t1, t2, file_name):
    t1 = t1 * 1000 #pydub fonctionne en milisecondes
    t2 = t2 * 1000
    newAudio = audio_file[t1:t2]
    newAudio.export(file_name, format='wav')
 # y : audio, sr : freq de l'audio
# print() # calcul de la hauteur
def get_chunks_info(c):
    f = wave.open(c, 'rb')
    y, sr = librosa.load(c)
    return (librosa.estimate_tuning(y=y, sr=sr),librosa.beat.tempo(y=y, sr=sr), np.max(np.abs(librosa.stft(y))))
audio = AudioSegment.from_wav('test2.wav')
j = 0
for i in range(5,int(audio.duration_seconds),5):
    name = ''.join(['chunks/part', str(i), '.wav'])
    create_chunk(audio, j,i, name)
    j = i
allchunks = [f for f in listdir('chunks/') if isfile(join('chunks/', f))]
for c in allchunks:
    print(get_chunks_info('chunks/' + c))


