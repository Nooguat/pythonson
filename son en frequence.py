import wave
sku = wave.open('sard.wav', 'rb')
print(sku.getnframes())
print(sku.getframerate())