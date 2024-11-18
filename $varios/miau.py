import simpleaudio as sa

# Cargamos el archivo de audio con el sonido de miau
wave_obj = sa.WaveObject.from_wave_file("habla.wav.wav")

# Reproducimos el sonido de miau
play_obj = wave_obj.play()

# Esperamos a que el sonido termine de reproducirse
play_obj.wait_done()