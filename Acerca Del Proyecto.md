# microvision ESPAÑOL
Un programa de adquisición de imágenes de soporte de alta resolución para microscopios ópticos usando una cámara web. Desarrollado con el lenguaje de programación Python y utilizando bibliotecas como Tkinter, OpenCV, NumPy, ctypes.wintypes, PIL, imutils, random, math, os, time y subprocess. El programa se desarrolló y probó originalmente en el sistema operativo Linux Manjaro de 64 bits. Para compatibilidad con Windows, la línea "cap = cv2.VideoCapture(x, cv2.CAP_V4L)" debe cambiarse a "cap = cv2.VideoCapture(x, cv2.CAP_DSHOW)". Actualmente, el programa se está porteando a un ejecutable .exe para Windows.

![texto alternativo](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

El programa presenta una interfaz gráfica de usuario (GUI) con botones para seleccionar la configuración actual del microscopio, como el objetivo y el ocular en uso. Al presionar el botón "Inicio", los usuarios pueden mostrar una región de interés (ROI). El programa también ofrece dos funciones de "Captura", incluida la capacidad de capturar el ROI en la resolución más alta disponible de la cámara en formato PNG y una función de "Capturar video" para capturar video en la resolución más alta y fotogramas por segundo que ofrece la cámara. El programa fue diseñado para trabajar con la cámara web 4K de GADNIC para lograr un ROI de 2020x2020 píxeles y captura de video H.265.

El programa también incluye una función de "Medir" que ejecuta el software ImageJ para el procesamiento de imágenes. Para que esta función sea posible, los scripts y archivos XML que lo acompañan deben estar ubicados en la carpeta raíz del software ImageJ, junto al ejecutable. ImageJ es un programa ampliamente utilizado en la comunidad científica para el procesamiento de micrografías y se puede descargar desde el siguiente enlace: https://imagej.nih.gov/ij/download.html.

El proyecto está diseñado para ser compatible con la mayoría de los sistemas de microscopía que pueden acomodar una cámara web en su ocular. El acoplamiento utilizado para la cámara web GADNIC se imprimió en 3D específicamente para un ocular de microscopio Arcano L101. Sin embargo, si se usa un ocular diferente y se necesita un adaptador, los usuarios pueden solicitar uno enviando un correo electrónico a lorenzotell1998@gmail.com con las dimensiones del ocular deseado. Luego, el diseñador creará un encaje personalizado para acomodar el ocular solicitado.

![texto alternativo](https://github.com/LorenzoTell/microvision/blob/main/adaptador.png)


# El programa de configuración del sistema cal.py

En el programa cal.py se deben seleccionar la cantidad de objetivos que posee el sistema. Luego se deben seleccionar el o los oculares a los cuales se les va a adaptar la cámara. Luego se debe cargar la información de cada objetivo y ocular para que el programa haga un cálculo del FOV. Luego de configurar los elementos del sistema, se procede a calibrar los ROI de cada configuración óptica, seleccione el ocular que se está utilizando actualmente y el objetivo, ejecute la rutina de calibración para que el programa automáticamente detecte el ROI de la circunferencia del tubo óptico. Esta información de encuadre se van a guardar en un archivo xml que luego serán utilizados en el programa principal para la captura de las imágenes, así que es primordial ejecutar esta rutina de calibración tantas veces como sea necesaria para que el sistema quede perfectamente alineado. En la rutina de calibración verá una ventana con la imágen del tubo óptico, y dos sliders, uno con el valor de umbralización para ajustar perfectamente la circunferencia y otro para aceptar el inicio de la rutina de deteccion

![alt text](https://github.com/LorenzoTell/microvision/blob/main/circuloCal.png)

Una vez detectado el ROI cuadrado, observe si el mismo encastra perfectamente, caso contrario repita la calibración.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/circuloFin.png)

Haga este proceso para cada combinación de ocular/objetivo que disponga. Puede comprobar cada ROI presionando el boton "INICIAR" y observando el recorte en tiempo real 
