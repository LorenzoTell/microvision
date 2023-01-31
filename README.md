# microvision ENGLISH
A high-resolution support image acquisition program for optical microscopes using a webcam. Developed using Python programming language and utilizing libraries such as Tkinter, OpenCV, NumPy, ctypes.wintypes, PIL, imutils, random, math, os, time, and subprocess. The program was originally developed and tested on Linux Manjaro 64-bits operating system. For Windows compatibility, the line "cap = cv2.VideoCapture(2, cv2.CAP_V4L)" should be changed to "cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)". The program is currently being ported to a .exe executable for Windows."

![alt text](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

The program features a graphical user interface (GUI) with buttons to select the current microscope settings, such as the objective and eyepiece in use. By pressing the "Start" button, users can display a region of interest (ROI). The program also offers two "Capture" functions, including the ability to capture the ROI in the highest resolution available from the camera in PNG format and a "Capture Video" function to capture video in the highest resolution and frames per second offered by the camera. The program was designed to work with the GADNIC webcam 4K to achieve an ROI of 2020x2020 pixels and H.265 video capture.

The program also includes a "Measure" function that runs the ImageJ software for image processing. For this function to work, the accompanying scripts and XML files must be located in the root folder of the ImageJ software, next to the executable. ImageJ is a widely used program in the scientific community for processing micrographs and can be downloaded from the following link: https://imagej.nih.gov/ij/download.html.

The project is designed to be compatible with most microscopy systems that can accommodate a webcam on their eyepiece. The coupling used for the GADNIC webcam was 3D printed specifically for an Arcano L101 microscope eyepiece. However, if a different eyepiece is used and an adapter is needed, users can request one by emailing lorenzotell1998@gmail.com with the dimensions of their desired eyepiece. The designer will then create a custom socket to accommodate the requested eyepiece.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/adaptador.png)
