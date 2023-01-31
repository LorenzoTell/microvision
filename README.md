# microvision ESPAÑOL
Programa de adquisición de imágenes tomadas con microscopios ópticos a los cuales se les adapta una camara web de alta resolución.
Corre con python, con las librerías Tkinter, opencv, numpy, ctypes.wintypes, PIL, imutils, random, math, os, time, subprocess. Programado en Linux. Si se va a utilizar en windows debe cambiarse "cap = cv2.VideoCapture(2, cv2.CAP_V4L)" por "cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)" 
Puede portearse a un ejecutable .exe para Windows // estamos trabajando en esto, hasta el momento, todas las funciones fueron testeadas en linux Manjaro 64bits

![alt text](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

El programa consta de una GUI con botones para seleccionar la configuración actual del microscopio (objetivo y ocular que se está usando) Mostrar una region de interes (ROI) al precionar el boton "Iniciar" y dos funciones "Capturar imágenes" que captura el ROI de la imágen en png en la mayor resolución que la cámara empleada pueda ofrecer y "capturar video" captura video en la mayor resolución y fps que la cámara pueda ofrecer. Nosotros elegimos la camara gadnic webcam 4k para obtener ROI de 2020x2020px y captura de video por h.265.

La funcion "Medir" ejecuta el software ImageJ, para que esto funcione, los scripts y los archivos xml que acompañan a este proyecto deben estar en la carpeta raíz del software ImageJ junto al ejecutable. ImageJ es un programa muy utilizado por la comunidad científica para el procesamiento de micrografías. Link: https://imagej.nih.gov/ij/download.html

El proyecto está pensado para poder utilizarse en la mayoría de los sistemas de microscopía a los cuales una cámara web pueda adaptarse al ocular del mismo. El acople que utilizamos nosotros para la gadnic fue impreso en 3D para un ocular de microscopio Arcano L101. Este no es un ocular estándar, si alguien necesitase un adaptador para la cámara gadnic puede escribir al mail lorenzotell1998@gmail.com con la petición, y las dimensiones del ocular que se pretende usar y sin problemas le puedo diseñar un encastre para el mismo.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/adaptador.png)


# microvision ENGLISH
Program for the acquisition of images taken with optical microscopes to which a high-resolution webcam is adapted.
It runs with python, with the Tkinter, opencv, numpy, ctypes.wintypes, PIL, imutils, random, math, os, time, subprocess libraries. Programmed in Linux. If it is going to be used in windows, "cap = cv2.VideoCapture(2, cv2.CAP_V4L)" should be changed to "cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)"
It can be ported to a .exe executable for Windows // we are working on this, so far, all functions have been tested on linux Manjaro 64bits

![alt text](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

The program consists of a GUI with buttons to select the current microscope settings (objective and eyepiece being used), display a region of interest (ROI) by pressing the "Start" button, and two "Capture Images" functions that capture the ROI. of the png image in the highest resolution that the camera used can offer and "capture video" captures video in the highest resolution and fps that the camera can offer. We chose the gadnic webcam 4k to get ROI of 2020x2020px and h.265 video capture.

The "Measure" function runs the ImageJ software, for this to work the scripts and xml files that accompany this project must be in the root folder of the ImageJ software next to the executable. ImageJ is a program widely used by the scientific community for processing micrographs. Link: https://imagej.nih.gov/ij/download.html

The project is designed to be used in most microscopy systems to which a webcam can be adapted to its eyepiece. The coupling we use for the gadnic was 3D printed for an Arcano L101 microscope eyepiece. This is not a standard eyepiece, if someone needs an adapter for the gadnic camera, they can write to lorenzotell1998@gmail.com with the request, and the dimensions of the eyepiece that they intend to use and without problems I can design a socket for it.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/adapter.png)


