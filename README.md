# microvision ENGLISH
A high-resolution support image acquisition program for optical microscopes using a webcam. Developed using Python programming language and utilizing libraries such as Tkinter, OpenCV, NumPy, ctypes.wintypes, PIL, imutils, random, math, os, time, and subprocess. The program was originally developed and tested on Linux Manjaro 64-bits operating system. For Windows compatibility, the line "cap = cv2.VideoCapture(2, cv2.CAP_V4L)" should be changed to "cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)". The program is currently being ported to a .exe executable for Windows."

![alt text](https://github.com/LorenzoTell/microvision/blob/main/GUI.png)

The program features a graphical user interface (GUI) with buttons to select the current microscope settings, such as the objective and eyepiece in use. By pressing the "Start" button, users can display a region of interest (ROI). The program also offers two "Capture" functions, including the ability to capture the ROI in the highest resolution available from the camera in PNG format and a "Capture Video" function to capture video in the highest resolution and frames per second offered by the camera. The program was designed to work with the GADNIC webcam 4K to achieve an ROI of 2020x2020 pixels and H.265 video capture.

The program also includes a "Measure" function that runs the ImageJ software for image processing. For this function to work, the accompanying scripts and XML files must be located in the root folder of the ImageJ software, next to the executable. ImageJ is a widely used program in the scientific community for processing micrographs and can be downloaded from the following link: https://imagej.nih.gov/ij/download.html.

The project is designed to be compatible with most microscopy systems that can accommodate a webcam on their eyepiece. The coupling used for the GADNIC webcam was 3D printed specifically for an Arcano L101 microscope eyepiece. However, if a different eyepiece is used and an adapter is needed, users can request one by emailing lorenzotell1998@gmail.com with the dimensions of their desired eyepiece. The designer will then create a custom socket to accommodate the requested eyepiece.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/adaptador.png)

# The system configuration program cal.py

In the cal.py program, you must select the number of objectives that the system has. Then you must select the eyepieces to which the camera will be adapted. Then the information of each objective and eyepiece must be loaded so that the program makes a calculation of the FOV. After configuring the elements of the system, proceed to calibrate the ROI of each optical configuration, select the eyepiece that is currently being used and the objective, run the calibration routine so that the program automatically detects the ROI of the circumference of the optical tube . This framing information will be saved in an xml file that will later be used in the main program to capture the images, so it is essential to run this calibration routine as many times as necessary so that the system is perfectly aligned. In the calibration routine you will see a window with the image of the optical tube, and two sliders, one with the threshold value to perfectly adjust the circumference and another to accept the start of the detection routine

![alt text](https://github.com/LorenzoTell/microvision/blob/main/circuloCal.png)

Once the square ROI is detected, see if it fits perfectly, otherwise repeat the calibration.

![alt text](https://github.com/LorenzoTell/microvision/blob/main/circuloFin.png)

Do this process for each eyepiece/objective combination you have. You can check each ROI by pressing the "START" button and watching the clipping in real time




