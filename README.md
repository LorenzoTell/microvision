# microvision ESPAÑOL
Programa de adquisición de imágenes tomadas con microscopios ópticos a los cuales se les adapta una camara web de alta resolución.
Corre con python, con las librerías Tkinter, opencv, numpy, ctypes.wintypes, PIL, imutils, random, math, os, time, subprocess. Programado en Linux. Si se va a utilizar en windows debe cambiarse "cap = cv2.VideoCapture(2, cv2.CAP_V4L)" por "cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)" 
Puede portearse a un ejecutable .exe para Windows // estamos trabajando en esto, hasta el momento, todas las funciones fueron testeadas en linux Manjaro 64bits

![alt text](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

El programa consta de una GUI con botones para seleccionar la configuración actual del microscopio (objetivo y ocular que se está usando) Mostrar una region de interes (ROI) al precionar el boton "Iniciar" y dos funciones "Capturar imágenes" que captura el ROI de la imágen en png en la mayor resolución que la cámara empleada pueda ofrecer y "capturar video" captura video en la mayor resolución y fps que la cámara pueda ofrecer. Nosotros elegimos la camara gadnic webcam 4k para obtener ROI de 2020x2020px y captura de video por h.265.

La funcion "Medir" ejecuta el software ImageJ, para que esto funcione, los scripts y los archivos xml que acompañan a este proyecto deben estar en la carpeta raíz del software ImageJ junto al ejecutable. ImageJ es un programa muy utilizado por la comunidad científica para el procesamiento de micrografías. Link: https://imagej.nih.gov/ij/download.html

El proyecto está pensado para poder utilizarse en la mayoría de los sistemas de microscopía a los cuales una cámara web pueda adaptarse al ocular del mismo. El acople que utilizamos nosotros para la gadnic fue impreso en 3D para un ocular de microscopio Arcano L101. Este no es un ocular estándar, si alguien necesitase un adaptador para la cámara gadnic puede escribir al mail lorenzotell1998@gmail.com con la petición, y las dimensiones del ocular que se pretende usar y sin problemas le puedo diseñar un encastre para el mismo.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/adaptador.png)





