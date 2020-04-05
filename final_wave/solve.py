import wave

file = wave.open(
    "data/Final.wav", mode='rb')

# print(file.getnframes())
file.readframes(8)
print(file.readframes(8))
file.readframes(8)
print(list(map(hex, file.readframes(16))))
