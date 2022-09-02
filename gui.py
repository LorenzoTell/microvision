from ctypes.wintypes import HGDIOBJ
from tkinter import *
from random import random
import tkinter
from PIL import Image
from PIL import ImageTk
import imutils
import cv2
import numpy as np
import time
import math
import matplotlib.pyplot as plt
global cap
global x
global y
global h
global w
x=0
y=0
h=0
w=0

cap = cv2.VideoCapture(2, cv2.CAP_V4L)
#cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FPS, 30.0)
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 10000) #3840
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000) #2160
a=0
estado=0 
root = Tk()

root.title('Digital Microvision')

#bg = PhotoImage(file='/home/lorenzo/Escritorio/Microcam/bk1.png')

pColor="blue"
elCanvas = Canvas(root, width=1024,height=600, bd=0 , highlightthickness=0)
elCanvas.pack(fill="both", expand=True)
#elCanvas.create_image(0,0, image=bg, anchor="nw")

#Funciones

def initCam():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, initCam)
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
        

        #print(np.shape(frame))
        # uint8 numpy.ndarray
        #frame=cv2.imread('a1.png')
        frameC=frame
        #cv2.imshow('Calibracion1', frameC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = apply_brightness_contrast(frame,100, 50)
        
        ajuste = 40
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

                    if -15 < offsetx < 15 and -15 < offsety < 15 :
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
                            roi = frameC[y:y+h,x:x+w]
                            #cv2.imshow('ROI', roi)
                            
                            #cv2.imwrite('pantalla.png',roi)
                            if f > 5: #130
                                loopCal=0
                                cap.release
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



def adquirir(x,y,h,w):
    pass

# Clases
class DrawLine:
    def __init__(self,master):
        #self.canvas = Canvas(master, width=500, height=500,bg="white")
        self.canvas = elCanvas
        #self.canvas.attributes('-alpha',0.5)
        self.canvas.bind("<Button-1>", lambda e: self._move(e.x,e.y))
        elCanvas.update()
        self.previous_pos = None
        self.total_length = 0
        self.t = Label(root, text=f"Longitud Total: {self.total_length} pixels",font=('Arial',12),pady=5,bg="DeepSkyBlue4",fg="white")
        ventana=self.t
        self.canvas.tag_raise("lineas")
        #self.t.pack(side="top", fill="both", expand=True)
        #self.canvas.pack(side="top", fill="both", expand=True)
        #self.t.place(relx=1.0, rely=1.0, x=-2, y=-2,anchor="se")
        #self.canvas.place(relx=1.0, rely=1.0, x=-2, y=-2,anchor="se")
        elCanvas.create_window(0,0, anchor="nw", window=ventana)
        #salva=elCanvas.create_window(0,0, anchor="nw", window=lineasventana)
        
        

    def _move(self,new_x,new_y):
        punto=1
        self.canvas.create_oval(new_x + punto, new_y + punto, new_x - punto, new_y - punto, width=0, fill='red', tags="lineas")
        if self.previous_pos:
            old_x, old_y = self.previous_pos
            self.canvas.create_line(old_x, old_y, new_x, new_y, width=2, fill='red', tags="lineas")
            self.total_length += ((new_x - old_x) ** 2 + (new_y - old_y) ** 2) ** (1 / 2)
            self.t.config(text=f"Longitud total: {round(self.total_length,2)} pixels")
        self.previous_pos = (new_x, new_y)
#Botones:


setCali = Button (root, text="Calibrar",font=("Helvetica", 20), command= lambda: calibracion(x,y,h,w))

setCali_w = elCanvas.create_window(850,40, anchor="nw", window=setCali)

setIni = Button (root, text="Iniciar",font=("Helvetica", 20), command= initCam)

setIni_w = elCanvas.create_window(850,100, anchor="nw", window=setIni)

setFoto = Button (root, text="Adquirir",font=("Helvetica", 20), command= lambda:adquirir(x,y,h,w))

setFoto_w = elCanvas.create_window(850,160, anchor="nw", window=setFoto)

#LA PARTE DE ESCRITURA ACA VA  UN LABEL PARA APAREZCANJ UNA VEZ ADQUIRIDA LA IMAGEN
setLin = Button (root, text="Linea",font=("Helvetica", 20), command= lambda: DrawLine(root))

setLin_w = elCanvas.create_window(850,240, anchor="nw", window=setLin)

setRec = Button (root, text="Rectangulo",font=("Helvetica", 20), command=0)

setRec_w = elCanvas.create_window(850,320, anchor="nw", window=setRec)

setCirc = Button (root, text="Circulo",font=("Helvetica", 20), command= 0)

setCirc_w = elCanvas.create_window(850,380, anchor="nw", window=setCirc)

#linea
#rectangulo
#circulo
elCanvas.update()
lblVideo = Label(root)
#lblVideo_w= elCanvas.create_window(0,0, anchor="nw", window=lblVideo, tags="video")
#lblVideo.pack(expand=True)
#lblVideo.pack(side = LEFT)




#x,y,h,w=calibracion(x,y,h,w)

root.mainloop()
