# Renvoie une valeur de la hauteur entre -0.5 et 0.5
import librosa # Librairie d'analyse de son
from pydub import AudioSegment# Librairie de modification de son
def create_chunk(audio_file, t1, t2, file_name):
    t1 = t1 * 1000 #pydub fonctionne en milisecondes
    t2 = t2 * 1000
    newAudio = audio_file[t1:t2]
    newAudio.export(file_name, format='wav')
y, sr = librosa.load('test.wav') # y : audio, sr : freq de l'audio
# print(librosa.estimate_tuning(y=y, sr=sr)) # calcul de la hauteur
def get_chunks_info(c):
    print(librosa.frequency_weighting(y))
audio = AudioSegment.from_wav('test.wav')
j = 0
for i in range(5,int(audio.duration_seconds),5):
    name = ''.join(['chunks/part', str(i), '.wav'])
    create_chunk(audio, j,i, name)
    j = i
