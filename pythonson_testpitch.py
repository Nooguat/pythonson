# Renvoie une valeur de la hauteur entre -0.5 et 0.5
import librosa
y, sr = librosa.load('test.wav')
print(librosa.estimate_tuning(y=y, sr=sr))