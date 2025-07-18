import numpy as np
import scipy.io.wavfile as wavfile
import os

# Crear una carpeta para guardar los sonidos
output_dir = "notas_sonido"
os.makedirs(output_dir, exist_ok=True)

# Frecuencias para notas en la octava 4
notas_frecuencias = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
}

# Parámetros del audio
duracion = 1.0  # en segundos
sample_rate = 44100  # muestras por segundo
t = np.linspace(0, duracion, int(sample_rate * duracion), endpoint=False)

# Generar archivos de audio
for nota, freq in notas_frecuencias.items():
    onda = 0.5 * np.sin(2 * np.pi * freq * t)
    audio = np.int16(onda * 32767)
    wavfile.write(os.path.join(output_dir, f"{nota}.wav"), sample_rate, audio)

print(f"Archivos guardados en la carpeta: {output_dir}")
