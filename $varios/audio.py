import scipy.io.wavefile as wav
import numpy as np

# Define la frecuencia de la señal y el número de muestras por segundo
frequency = 440
sample_rate = 44100

# Genera una señal senoidal de 1 segundo de duración
t = np.linspace(0, 1, sample_rate, False)
signal = np.sin(2 * np.pi * frequency * t)

# Convierte la señal a enteros de 16 bits
signal = np.array(signal * 32767, dtype='int16')

# Escribe la señal a un archivo de audio .wav
wav.write("sine.wav", sample_rate, signal)
