#!/usr/bin/env python3
from ctypes.wintypes import HGDIOBJ
from tkinter import *
from tkinter import filedialog
from random import random
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import imutils
import cv2
import numpy as np
import time
import math
import xml.etree.ElementTree as ET
import os
import subprocess
import configparser
import datetime
import tifffile as tiff

global cap
global x
global y
global h
global w

global objetivo1
global objetivo2
global objetivo3
global objetivo4
global ocular1
global ocular2



##################################### Calibración paramétrica del sistema ################################

cantidadObjetivos = 3
cantidadOcular = 1


objetivo1 = 4
objetivo2 = 20
objetivo3 = 50
objetivo4 = 0

ocular1=20
ocular2=0

#Unidad pixeles/mm
relacion11 = 1528
relacion12 = 5000
relacion13 = 12657.27273
relacion14 = "4"

relacion21 = "0"
relacion22 = "0"
relacion23 = "0"
relacion24 = "0"
default_index=0 # Index global de la cámara, si usted posee otro dispositivo de video conectado, use el número 2.



######################## droidcam ##############

#env ANDROID_SERIAL=330021f5a2b235fb droidcam-cli adb 4747
#https://www.dev47apps.com/droidcam/linux/


###########################################################################################################





x=0
y=0
h=0
w=0
video=0




cap = cv2.VideoCapture(default_index, cv2.CAP_V4L2)
#cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS, 30.0)
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc(*"H265"))# *"MJPG" - *'H265'
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840) #3840
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160) #2160

a=0
estado=0 
root = Tk()

root.title('Digital Microvision')

file_path = "dimensions.xml"

if os.path.exists(file_path):
    print(f'{file_path} exists')
else:
    raiz = ET.Element("raiz")

    ocular_xml_1 = ET.SubElement(raiz, "ocular_xml_1")
    objetivo1_o1 = ET.SubElement(ocular_xml_1, "objetivo1")
    objetivo2_o1 = ET.SubElement(ocular_xml_1, "objetivo2")
    objetivo3_o1 = ET.SubElement(ocular_xml_1, "objetivo3")
    objetivo4_o1 = ET.SubElement(ocular_xml_1, "objetivo4")

    ocular_xml_2 = ET.SubElement(raiz, "ocular_xml_2")
    objetivo1_o2 = ET.SubElement(ocular_xml_2, "objetivo1")
    objetivo2_o2 = ET.SubElement(ocular_xml_2, "objetivo2")
    objetivo3_o2 = ET.SubElement(ocular_xml_2, "objetivo3")
    objetivo4_o2 = ET.SubElement(ocular_xml_2, "objetivo4")

    ET.SubElement(objetivo1_o1, "x").text = str(x)
    ET.SubElement(objetivo1_o1, "y").text = str(y)
    ET.SubElement(objetivo1_o1, "h").text = str(h)
    ET.SubElement(objetivo1_o1, "w").text = str(w)

    ET.SubElement(objetivo2_o1, "x").text = str(x)
    ET.SubElement(objetivo2_o1, "y").text = str(y)
    ET.SubElement(objetivo2_o1, "h").text = str(h)
    ET.SubElement(objetivo2_o1, "w").text = str(w)

    ET.SubElement(objetivo3_o1, "x").text = str(x)
    ET.SubElement(objetivo3_o1, "y").text = str(y)
    ET.SubElement(objetivo3_o1, "h").text = str(h)
    ET.SubElement(objetivo3_o1, "w").text = str(w)

    ET.SubElement(objetivo4_o1, "x").text = str(x)
    ET.SubElement(objetivo4_o1, "y").text = str(y)
    ET.SubElement(objetivo4_o1, "h").text = str(h)
    ET.SubElement(objetivo4_o1, "w").text = str(w)

    ET.SubElement(objetivo1_o2, "x").text = str(x)
    ET.SubElement(objetivo1_o2, "y").text = str(y)
    ET.SubElement(objetivo1_o2, "h").text = str(h)
    ET.SubElement(objetivo1_o2, "w").text = str(w)

    ET.SubElement(objetivo2_o2, "x").text = str(x)
    ET.SubElement(objetivo2_o2, "y").text = str(y)
    ET.SubElement(objetivo2_o2, "h").text = str(h)
    ET.SubElement(objetivo2_o2, "w").text = str(w)

    ET.SubElement(objetivo3_o2, "x").text = str(x)
    ET.SubElement(objetivo3_o2, "y").text = str(y)
    ET.SubElement(objetivo3_o2, "h").text = str(h)
    ET.SubElement(objetivo3_o2, "w").text = str(w)

    ET.SubElement(objetivo4_o2, "x").text = str(x)
    ET.SubElement(objetivo4_o2, "y").text = str(y)
    ET.SubElement(objetivo4_o2, "h").text = str(h)
    ET.SubElement(objetivo4_o2, "w").text = str(w)

    tree = ET.ElementTree(raiz)
    tree.write("dimensions.xml")



#bg = PhotoImage(file='/home/lorenzo/MEGAsync/Microcam/bkai3.png')
bg = PhotoImage(file='bkai3.png')
pColor="blue"
elCanvas = Canvas(root, width=1024,height=720, bd=0 , highlightthickness=0)
elCanvas.pack(fill="both", expand=True)
elCanvas.create_image(0,0, image=bg, anchor="nw")

#Funciones

def initCam():
    global cap

    tree = ET.parse("dimensions.xml")
    raiz = tree.getroot()
    if (bOcular1_estado == True):
        ocular_xml_1 = raiz.find("ocular_xml_1")
        if (bObjetivo1_estado == True):
            objetivo1_o1 = ocular_xml_1.find('objetivo1')
            x = objetivo1_o1.find('x')
            y = objetivo1_o1.find('y')
            h = objetivo1_o1.find('h')
            w = objetivo1_o1.find('w')
        if (bObjetivo2_estado == True):
            objetivo2_o1 = ocular_xml_1.find('objetivo2')
            x = objetivo2_o1.find('x')
            y = objetivo2_o1.find('y')
            h = objetivo2_o1.find('h')
            w = objetivo2_o1.find('w')
        if (bObjetivo3_estado == True):
            objetivo3_o1 = ocular_xml_1.find('objetivo3')
            x = objetivo3_o1.find('x')
            y = objetivo3_o1.find('y')
            h = objetivo3_o1.find('h')
            w = objetivo3_o1.find('w')
        if (bObjetivo4_estado== True):
            objetivo4_o1 = ocular_xml_1.find('objetivo4')
            x = objetivo4_o1.find('x')
            y = objetivo4_o1.find('y')
            h = objetivo4_o1.find('h')
            w = objetivo4_o1.find('w')
    if (bOcular2_estado == True):
        ocular_xml_2 = raiz.find("ocular_xml_2")
        if (bObjetivo1_estado == True):
            objetivo1_o2 = ocular_xml_2.find('objetivo1')
            x = objetivo1_o2.find('x')
            y = objetivo1_o2.find('y')
            h = objetivo1_o2.find('h')
            w = objetivo1_o2.find('w')
        if (bObjetivo2_estado == True):
            objetivo2_o2 = ocular_xml_2.find('objetivo2')
            x = objetivo2_o2.find('x')
            y = objetivo2_o2.find('y')
            h = objetivo2_o2.find('h')
            w = objetivo2_o2.find('w')
        if (bObjetivo3_estado == True):
            objetivo3_o2 = ocular_xml_2.find('objetivo3')
            x = objetivo3_o2.find('x')
            y = objetivo3_o2.find('y')
            h = objetivo3_o2.find('h')
            w = objetivo3_o2.find('w')
        if (bObjetivo4_estado== True):
            objetivo4_o2 = ocular_xml_2.find('objetivo4')
            x = objetivo4_o2.find('x')
            y = objetivo4_o2.find('y')
            h = objetivo4_o2.find('h')
            w = objetivo4_o2.find('w')
    x = int(x.text)
    y = int(y.text)
    h = int(h.text)
    w = int(w.text)

    if cap is not None:

        ret, frame = cap.read()
        frame = frame[y:y+h,x:x+w]
        if ret == True:

            if bOcular1_estado == True:
                ajuste = 40
                width = int(frame.shape[1] * ajuste / 100)
                height = int(frame.shape[0] * ajuste / 100)
                dim = (width, height)
                frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(100, initCam)
            elCanvas.create_image(0,0, image=img, anchor="nw")
            elCanvas.tag_lower("video")
        else:
            lblVideo.image = ""
            cap.release()


def calibracion(x,y,h,w):

    def f(d):
        pass
    cv2.namedWindow('Calibracion')

    
    t=cv2.createTrackbar('Threshold','Calibracion', 80, 255, f)
    switch= 'Aceptar'
    s=cv2.createTrackbar(switch,'Calibracion', 0, 1, f)
   
    
  
    def apply_brightness_contrast(input_img,  brightness=0, contrast=0):
        if brightness != 0:
            if brightness > 0:
                shadow = brightness
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + brightness
            alpha_b = (highlight - shadow)/255
            gamma_b = shadow

            buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
        else:
            buf = input_img.copy()

        if contrast != 0:
            f = 131*(contrast + 127)/(127*(131-contrast))
            alpha_c = f
            gamma_c = 127*(1-f)

            buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

        return buf
    
    lista=[]
    coseno = math.radians (45)
    coseno = math.cos (coseno)
    seno = math.radians (45)
    seno = math.sin (seno)
   
    loopCal=1

    while loopCal:
        elCanvas.update()
        ret, frame = cap.read()
        color= (0,0,0)
        #elCanvas.update()
        

        print(np.shape(frame))
        # uint8 numpy.ndarray
        #frame=cv2.imread('a1.png')
        frameC=frame
        #cv2.imshow('Calibracion1', frameC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = apply_brightness_contrast(frame,100, 50)
        
        ajuste = 15
        width = int(frame.shape[1] * ajuste / 100)
        height = int(frame.shape[0] * ajuste / 100)
        dim = (width, height)

        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        edge = cv2.threshold(frame, t,255, cv2.THRESH_BINARY)[1]
        edge = cv2.GaussianBlur(edge, (7, 7), 15)
        rows = edge.shape[0]
        
        if s == 0:
            cv2.imshow('Calibracion', edge)
    

        if s == 1:
            texto="Calibrando por favor espere"
            ubicacion=(65,100)
            font=cv2.FONT_HERSHEY_SIMPLEX
            tamLetra=0.8
            grosor=1
            cv2.imshow('Calibracion', frame)
            circles = cv2.HoughCircles(edge, cv2.HOUGH_GRADIENT, 1, rows / 8,param1=1, param2=1,minRadius=100, maxRadius=1000)

            ancho2 = int(frame.shape[1] /2)
            alto2 = int(frame.shape[0] /2)
            ancho = int(frame.shape[1])
            alto = int(frame.shape[0])
            centroimg = (ancho2,alto2)


            if circles is not None:

                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    #a=a+1
                    
                    center = (i[0], i[1])
                    
                    thickness=1
                    offsetx= ancho2 - i[0]
                    offsety= alto2 - i[1]
                    offsetGeneral = 30

                    if -offsetGeneral < offsetx < offsetGeneral and -offsetGeneral < offsety < offsetGeneral :
                        # circulo centro
                        #-----------   A partir de aca tomar los centros eh, y generar la media que va a utilizar lo de abajo para dibujar------


                        lista.append((i[0],i[1],i[2]))

                        #cv2.circle(frame, center, 2, color, 3)
                        # circulo
                        radius = i[2]
                        #cv2.circle(frame, center, radius, color, 1)

                        #hm=radius*seno
                        #of=radius*coseno
                        #print('Centro:', radius)
                        #sp=(int(i[0]-of), int(i[1]+hm))
                        #fp=(int(i[0]+of), int(i[1]-hm))
                        #cv2.circle(frame, sp, 2, color, 1)
                        #cv2.circle(frame, fp, 2, color, 1)
                        #print ('Punto inicial:',sp)
                        #print ('Punto inicial:',fp)
                        #print ('Matriz de datos')
                        #print ('')
                        #cv2.rectangle(frame,sp,fp,color,1)
                        f,k=np.shape(lista)
                        k=str(f) + "%"
                        ubicacion2=(235,140)
                        if f <= 100:
                            cv2.putText(frame, texto, ubicacion, font, tamLetra, color, grosor, bottomLeftOrigin = False)
                            cv2.putText(frame, k, ubicacion2, font, tamLetra, color, grosor, bottomLeftOrigin = False)
                        x=0
                        y=0
                        radio=0

                        cv2.imshow('Calibracion', frame)
                        
                        
                        if f > 2: #100

                            (total,a)=np.shape(lista)
                            for j in lista[:]:
                                x=j[0]+x
                                y=j[1]+y
                                radio=j[2]+radio

                            xt=int(x/total)
                            yt=int(y/total)
                            rt=int(radio/total)
                            center1= (xt,yt)
                            cv2.circle(frame, center1, 2, color, 3)
                            
                            #elCanvas.update()
                            hm=int(rt*seno)
                            of=int(rt*coseno)
                            #print('Centro:', radius)
                            sp=(xt-of, yt+hm)
                            fp=(xt+of, yt-hm)
                            #sp=(int((x/total)-(rt*coseno)), int((y/total)+(rt*seno)))
                            #fp=(int((x/total)+(rt*coseno)), int((y/total)-(rt*seno)))
                            # circulo
                            cv2.circle(frame, center1, rt, color, 1)
                            cv2.rectangle(frame,sp,fp,color,1)
                            cv2.imshow('Calibracion', frame)

                            ajuste1=ajuste/100
                            xtr=int(xt/ajuste1)
                            ytr=int(yt/ajuste1)
                            hmr=int(hm/ajuste1)
                            ofr=int(of/ajuste1)
                            #hmr=int(((radio/total)*seno)/ajuste1)
                            #ofr=int(((radio/total)*coseno)/ajuste1)
                            #cv2.circle(frame, sp, 2, color, 1)
                            #cv2.circle(frame, fp, 2, color, 1)
                            #print ('Punto inicial:',sp)
                            #print ('Punto inicial:',fp)
                            #print ('Matriz de datos')
                            #print ('')
                            
                            #print((xt,yt,rt))
                            x=xtr-ofr
                            y=ytr-hmr
                            h=2*hmr
                            w=2*ofr
                            if (h>alto):
                                roi = frameC[y:y,x:x+w]
                            roi = frameC[y:y+h,x:x+w]
                            #cv2.imshow('ROI', roi)
                            
                            cv2.imwrite('pantalla.png',roi)
                            if f > 3: #130
                                loopCal=0
                                cap.release
                                tree = ET.parse("dimensions.xml")
                                raiz = tree.getroot()
                                if (bOcular1_estado == True):
                                    ocular_xml_1 = raiz.find("ocular_xml_1")
                                    if (bObjetivo1_estado == True):
                                        objetivo1_o1 = ocular_xml_1.find('objetivo1')
                                        xv = objetivo1_o1.find('x')
                                        yv = objetivo1_o1.find('y')
                                        hv = objetivo1_o1.find('h')
                                        wv = objetivo1_o1.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo2_estado == True):
                                        objetivo2_o1 = ocular_xml_1.find('objetivo2')
                                        xv = objetivo2_o1.find('x')
                                        yv = objetivo2_o1.find('y')
                                        hv = objetivo2_o1.find('h')
                                        wv = objetivo2_o1.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo3_estado == True):
                                        objetivo3_o1 = ocular_xml_1.find('objetivo3')
                                        xv = objetivo3_o1.find('x')
                                        yv = objetivo3_o1.find('y')
                                        hv = objetivo3_o1.find('h')
                                        wv = objetivo3_o1.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo4_estado== True):
                                        objetivo4_o1 = ocular_xml_1.find('objetivo4')
                                        xv = objetivo4_o1.find('x')
                                        yv = objetivo4_o1.find('y')
                                        hv = objetivo4_o1.find('h')
                                        wv = objetivo4_o1.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")

                                if (bOcular2_estado == True):
                                    ocular_xml_2 = raiz.find("ocular_xml_2")
                                    if (bObjetivo1_estado == True):
                                        objetivo1_o2 = ocular_xml_2.find('objetivo1')
                                        xv = objetivo1_o2.find('x')
                                        yv = objetivo1_o2.find('y')
                                        hv = objetivo1_o2.find('h')
                                        wv = objetivo1_o2.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo2_estado == True):
                                        objetivo2_o2 = ocular_xml_2.find('objetivo2')
                                        xv = objetivo2_o2.find('x')
                                        yv = objetivo2_o2.find('y')
                                        hv = objetivo2_o2.find('h')
                                        wv = objetivo2_o2.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo3_estado == True):
                                        objetivo3_o2 = ocular_xml_2.find('objetivo3')
                                        xv = objetivo3_o2.find('x')
                                        yv = objetivo3_o2.find('y')
                                        hv = objetivo3_o2.find('h')
                                        wv = objetivo3_o2.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                    if (bObjetivo4_estado== True):
                                        objetivo4_o2 = ocular_xml_2.find('objetivo4')
                                        xv = objetivo4_o2.find('x')
                                        yv = objetivo4_o2.find('y')
                                        hv = objetivo4_o2.find('h')
                                        wv = objetivo4_o2.find('w')
                                        xv.text = str(x)
                                        yv.text = str(y)
                                        hv.text = str(h)
                                        wv.text = str(w)
                                        tree.write("dimensions.xml")
                                time.sleep(3)

                                print("completado")
                                cv2.destroyWindow('Calibracion')


                                


                                return x,y,h,w
                                

                                #lista=[]
                            
                            break

            
            #edge = cv2.line(edge, (0,alto2), (ancho,alto2), color, thickness) #horizontal
            #edge = cv2.line(edge, (ancho2,0) , (ancho2,alto), color, thickness) #vertical
            #cv2.imshow('Binario', edge)

            
            #time.sleep(0.3)


        if cv2.waitKey(20) == ord('q'):
                break
        t = cv2.getTrackbarPos('Threshold','Calibracion')
        s = cv2.getTrackbarPos(switch,'Calibracion')
        
    pass

def white_balance():
    stabilize=False
    #cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
    mean_brightness_ant=0
    while stabilize:
        # Capture a frame from the webcam
        ret, frame4k = cap.read()
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame4k, cv2.COLOR_BGR2GRAY)

        intensity_value = gray[5, 5]
        print(intensity_value)

        if intensity_value == 0:
            stabilize = False
            time.sleep(2)


    capture_webcam_frame()
    pass


def metaDataF(parser):
    global metadata
    global time_str
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    # Define the TIFF metadata
    metadata = { "scale":str(parser), "time": time_str }
    pass

def capture_webcam_frame():
    global metadata
    global time_str

    ret, frame4k = cap.read()

    tree = ET.parse("dimensions.xml")
    raiz = tree.getroot()
    if (bOcular1_estado == True):
        ocular_xml_1 = raiz.find("ocular_xml_1")
        if (bObjetivo1_estado == True):
            calibration=metaDataF(relacion11)
            objetivo1_o1 = ocular_xml_1.find('objetivo1')
            x = objetivo1_o1.find('x')
            y = objetivo1_o1.find('y')
            h = objetivo1_o1.find('h')
            w = objetivo1_o1.find('w')
        if (bObjetivo2_estado == True):
            calibration=metaDataF(relacion12)
            objetivo2_o1 = ocular_xml_1.find('objetivo2')
            x = objetivo2_o1.find('x')
            y = objetivo2_o1.find('y')
            h = objetivo2_o1.find('h')
            w = objetivo2_o1.find('w')
        if (bObjetivo3_estado == True):
            calibration=metaDataF(relacion13)
            objetivo3_o1 = ocular_xml_1.find('objetivo3')
            x = objetivo3_o1.find('x')
            y = objetivo3_o1.find('y')
            h = objetivo3_o1.find('h')
            w = objetivo3_o1.find('w')
        if (bObjetivo4_estado== True):
            calibration=metaDataF(relacion14)
            objetivo4_o1 = ocular_xml_1.find('objetivo4')
            x = objetivo4_o1.find('x')
            y = objetivo4_o1.find('y')
            h = objetivo4_o1.find('h')
            w = objetivo4_o1.find('w')
    if (bOcular2_estado == True):
        ocular_xml_2 = raiz.find("ocular_xml_2")
        if (bObjetivo1_estado == True):
            calibration=metaDataF(relacion21)
            objetivo1_o2 = ocular_xml_2.find('objetivo1')
            x = objetivo1_o2.find('x')
            y = objetivo1_o2.find('y')
            h = objetivo1_o2.find('h')
            w = objetivo1_o2.find('w')
        if (bObjetivo2_estado == True):
            calibration=metaDataF(relacion22)
            objetivo2_o2 = ocular_xml_2.find('objetivo2')
            x = objetivo2_o2.find('x')
            y = objetivo2_o2.find('y')
            h = objetivo2_o2.find('h')
            w = objetivo2_o2.find('w')
        if (bObjetivo3_estado == True):
            calibration=metaDataF(relacion23)
            objetivo3_o2 = ocular_xml_2.find('objetivo3')
            x = objetivo3_o2.find('x')
            y = objetivo3_o2.find('y')
            h = objetivo3_o2.find('h')
            w = objetivo3_o2.find('w')
        if (bObjetivo4_estado== True):
            calibration=metaDataF(relacion24)
            objetivo4_o2 = ocular_xml_2.find('objetivo4')
            x = objetivo4_o2.find('x')
            y = objetivo4_o2.find('y')
            h = objetivo4_o2.find('h')
            w = objetivo4_o2.find('w')

    x = int(x.text)
    y = int(y.text)
    h = int(h.text)
    w = int(w.text)

    frame4k = frame4k[y:y+h,x:x+w]
    frame4k =cv2.cvtColor(frame4k, cv2.COLOR_BGR2RGB)
    width = int(cap.get(3))
    height = int(cap.get(4))
    print("Resolution: {}x{}".format(width, height))
    # Create a Tkinter window
    root = tk.Tk()
    root.withdraw()
    # Ask the user to select a location to save the file
    filename = f"Img_{time_str}.tiff"
    filepath = filedialog.asksaveasfilename(defaultextension=".tiff", filetypes=[("TIFF", "*.tiff")], initialfile=filename,title='Guardar captura de imagen')


    # Save the frame as a TIFF image
    tiff.imwrite(filename, frame4k, metadata=metadata)

    #cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'H265'))

    pass

def capture_webcam_video(): #VIDEO REC ///////////////////////////////////////////////////////////////////////////////////////////
    video=1
    elCanvas.delete("start")

    setVid2 = Button (root, text="Stop",font=("Helvetica", 20), command= lambda:regenerarBotonVideo())

    setVid2_w = elCanvas.create_window(750,120, anchor="nw", window=setVid2, tags="stop")

    elCanvas.update()

    pass

def regenerarBotonVideo():
    elCanvas.delete("stop")
    elCanvas.update()
    setVid_w = elCanvas.create_window(750,120, anchor="nw", window=setVid,tags="start")
    pass

def medirImagej(): #ImageJ /////////////////////////////////////////////////////////////////////////////////////////////////////
    script_dir = os.path.dirname(os.path.abspath(__file__))
    executable_path = os.path.join(script_dir, "ImageJ")
    subprocess.run([executable_path])
    elCanvas.update()
    pass

def setOb1_press():
    global bObjetivo1_estado
    global bObjetivo2_estado
    global bObjetivo3_estado
    global bObjetivo4_estado

    setOb1.config(bg = "green")
    setOb2.config(bg = "red")
    setOb3.config(bg = "red")
    setOb4.config(bg = "red")
    bObjetivo1_estado = True
    bObjetivo2_estado = False
    bObjetivo3_estado = False
    bObjetivo4_estado= False
    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    pixelmm()



def setOb2_press():
    global bObjetivo1_estado
    global bObjetivo2_estado
    global bObjetivo3_estado
    global bObjetivo4_estado
    setOb1.config(bg = "red")
    setOb2.config(bg = "green")
    setOb3.config(bg = "red")
    setOb4.config(bg = "red")
    bObjetivo1_estado = False
    bObjetivo2_estado = True
    bObjetivo3_estado = False
    bObjetivo4_estado= False
    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    pixelmm()


def setOb3_press():
    global bObjetivo1_estado
    global bObjetivo2_estado
    global bObjetivo3_estado
    global bObjetivo4_estado
    setOb1.config(bg = "red")
    setOb2.config(bg = "red")
    setOb3.config(bg = "green")
    setOb4.config(bg = "red")
    bObjetivo1_estado = False
    bObjetivo2_estado = False
    bObjetivo3_estado = True
    bObjetivo4_estado= False
    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    pixelmm()

def setOb4_press():
    global bObjetivo1_estado
    global bObjetivo2_estado
    global bObjetivo3_estado
    global bObjetivo4_estado
    setOb1.config(bg = "red")
    setOb2.config(bg = "red")
    setOb3.config(bg = "red")
    setOb4.config(bg = "green")
    bObjetivo1_estado = False
    bObjetivo2_estado = False
    bObjetivo3_estado = False
    bObjetivo4_estado= True
    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    pixelmm()

def setOc1_press():
    global bObjetivo1_estado
    global bObjetivo2_estado
    global bObjetivo3_estado
    global bObjetivo4_estado
    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    global bOcular1_estado
    global bOcular2_estado
    setOc1.config(bg = "green")
    setOc2.config(bg = "red")
    bOcular1_estado = True
    bOcular2_estado= False

def setOc2_press():

    elCanvas.delete("adv1")
    elCanvas.delete("relacion")
    global bOcular1_estado
    global bOcular2_estado
    setOc1.config(bg = "red")
    setOc2.config(bg = "green")
    bOcular1_estado = False
    bOcular2_estado= True



def pixelmm():
    if (bOcular1_estado == True):
        if (bObjetivo1_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion11)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo2_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion12)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo3_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion13)+" pixeles/mm",font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo4_estado== True):
            elCanvas.create_text(870, 490, text=str(relacion14)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")
    if (bOcular2_estado == True):
        if (bObjetivo1_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion21)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo2_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion22)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo3_estado == True):
            elCanvas.create_text(870, 490, text=str(relacion23)+" pixeles/mm",font=("Helvetica", 20),fill="#800020", tags="relacion")
        if (bObjetivo4_estado== True):
            elCanvas.create_text(870, 490, text=str(relacion24)+" pixeles/mm", font=("Helvetica", 20),fill="#800020", tags="relacion")


    pass
#Botones:




setIni = Button (root, text="Iniciar",font=("Helvetica", 20), command= initCam)

setIni_w = elCanvas.create_window(750,30, anchor="nw", window=setIni)


setFoto = Button (root, text="Capturar Imagen",font=("Helvetica", 20), command= lambda:white_balance())

setFoto_w = elCanvas.create_window(750,75, anchor="nw", window=setFoto)

setVid = Button (root, text="Capturar Video",font=("Helvetica", 20), command= lambda:capture_webcam_video())

setVid_w = elCanvas.create_window(750,120, anchor="nw", window=setVid, tags="start")


setMedir = Button (root, text="Medir",font=("Helvetica", 20), command= medirImagej)

setMedir_w = elCanvas.create_window(860,30, anchor="nw", window=setMedir)



#Botones de los lentes

setOb1 = Button (root, text="x"+str(objetivo1),font=("Helvetica", 20), bg="red", command= lambda:setOb1_press())

setOb2 = Button (root, text="x"+str(objetivo2),font=("Helvetica", 20), bg="red",command= lambda:setOb2_press())

setOb3 = Button (root, text="x"+str(objetivo3),font=("Helvetica", 20),bg="red", command= lambda:setOb3_press())

setOb4 = Button (root, text="x"+str(objetivo4),font=("Helvetica", 20),bg="red", command= lambda:setOb4_press())

setOc1 = Button (root, text="x"+str(ocular1),font=("Helvetica", 20), bg="red",command= lambda:setOc1_press())

setOc2 = Button (root, text="x"+str(ocular2),font=("Helvetica", 20), bg="red",command= lambda:setOc2_press())

for i in range(cantidadObjetivos):
    if (i == 0):
        setOb1_w = elCanvas.create_window(750,207,anchor="nw", window=setOb1)
    if (i == 1):
        setOb2_w = elCanvas.create_window(830,207, anchor="nw", window=setOb2)
    if (i == 2):
        setOb3_w = elCanvas.create_window(750,252, anchor="nw", window=setOb3)
    if (i == 3):
        setOb4_w = elCanvas.create_window(825,252, anchor="nw", window=setOb4)

for i in range(cantidadOcular):
    if (i == 0):
        setOc1_w = elCanvas.create_window(750,334, anchor="nw", window=setOc1)
    if (i == 1):
        setOc2_w = elCanvas.create_window(810,334, anchor="nw", window=setOc2)





setCali = Button (root, text="Calibrar visor",font=("Helvetica", 20), command= lambda: calibracion(x,y,h,w))

setCali_w = elCanvas.create_window(750,384, anchor="nw", window=setCali)

#textos

elCanvas.create_text(805, 190, text="Objetivos:", font=("Helvetica", 20),fill="white")

elCanvas.create_text(805, 320, text="Oculares:", font=("Helvetica", 20),fill="white")

elCanvas.create_text(860, 455, text="Relación pixel/mm:", font=("Helvetica", 20),fill="white")

elCanvas.create_text(870, 490, text="Selecciona un objetivo y un ocular \n para establecer la relacion pixel/mm", font=("Helvetica", 12),fill="#800020", tags="adv1")


#LA PARTE DE ESCRITURA ACA VA  UN LABEL PARA APAREZCANJ UNA VEZ ADQUIRIDA LA IMAGEN

#setLin = Button (root, text="Linea",font=("Helvetica", 20), command= lambda: DrawLine(root))

#setLin_w = elCanvas.create_window(850,240, anchor="nw", window=setLin)

#setRec = Button (root, text="Rectangulo",font=("Helvetica", 20), command=0)

#setRec_w = elCanvas.create_window(850,320, anchor="nw", window=setRec)

#setCirc = Button (root, text="Circulo",font=("Helvetica", 20), command= 0)

#setCirc_w = elCanvas.create_window(850,380, anchor="nw", window=setCirc)

#linea
#rectangulo
#circulo

if (video==0):
    elCanvas.delete("stop")


elCanvas.update()
lblVideo = Label(root)
#lblVideo_w= elCanvas.create_window(0,0, anchor="nw", window=lblVideo, tags="video")
#lblVideo.pack(expand=True)
#lblVideo.pack(side = LEFT)

root.mainloop()
