import mediapipe as mp
import numpy as np
import PIL.Image as Image
mp_holistic = mp.solutions.holistic

holistic = mp_holistic.Holistic(static_image_mode=True)
for idx, file in enumerate(['/path/to/pic.jpg', '/path/to/pic2.jpg']):
  pic = Image.open(file)
  image_data = np.frombuffer(pic.tobytes(), dtype=np.uint8)
  image = np.copy(image_data.reshape((image_height, image_width, 3))[:,:,::-1])
  image_height, image_width, _ = image.shape
  results = holistic.process(image)
  if results.pose_landmarks:
    print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]\
 .x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]\
 .y * image_height})'
    )
holistic.close()



  Could not find a version that satisfies the requirement mediapipe (from cvzone) (from versions: )
No matching distribution found for mediapipe (from cvzone)


Install OpenCv: sudo bash ./mediapipe/setup_opencv.sh

CVZone:
Este es un paquete de visión por computadora que facilita la ejecución de funciones de procesamiento de imágenes e inteligencia artificial. Básicamente, En su Core usa bibliotecas OpenCV y Librerias de Mediapipe.


https://pythonrepo.com/repo/cvzone-cvzone
https://github.com/google/mediapipe
https://pypi.org/project/cvzone/
https://medium.com/analytics-vidhya/mediapipe-hand-gesture-based-volume-controller-in-python-w-o-gpu-67db1f30c6ed
https://www.youtube.com/results?search_query=different+stanadard+ESp+ESP+now
https://www.youtube.com/watch?v=w4R9VoY96h8

https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
https://www.youtube.com/watch?v=yqkISICHH-U
https://inteligencia.tech/
https://www.youtube.com/watch?v=v_cwOq06g9E
https://pypi.org/project/opencv-contrib-python/
https://www.codeproject.com/Articles/1274094/Capturing-Images-from-Camera-using-Python-and-Dire

