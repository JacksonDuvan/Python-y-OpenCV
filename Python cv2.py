import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)

while(captura.isOpened()):

    #Capturamos una imagen y la convertimos de RGB -> HSV
    ret, imagen = captura.read()

    if (ret):
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        h,w,m=imagen.shape
        
        #En este caso una pelota tennis 
        bajos = np.array([30,80,80], dtype=np.uint8)
        altos = np.array([40, 255, 255], dtype=np.uint8)
        

        #Crear una mascara con solo los pixeles dentro del rango 
        mask = cv2.inRange(hsv,bajos,altos)
        #Encontrar el area de los objetos que detecta la camara
        moments = cv2.moments(mask)
        area =int( moments['m00'])
        #Descomentar para ver el area por pantalla, inicia valores de coordenadas a '0'
        #print area
        x=0
        y=0
        dist=0

        if(area > 100000):
            #Buscamos el centro x, y del objeto
            x = int(moments['m10']/moments['m00'])
            y = int(moments['m01']/moments['m00'])
           
            #se realizan calculos para definir la distancia respecto al area
            if area>=845695.7:
                if area>=2301333.5:
                    dist=-(area/307781.175)+37.4771743
            if area<2301333.5:
                if area>=859737.4:
                  dist=-(area/72079.83)+61.9275725  
            if area<859737.4:
                dist=-(area/19652.8425)+93.74622211
            if int(dist)<=15:
                dist=15
            if int(dist)>=70:
                dist=70   
            #Mostramos sus coordenadas y distancia de la pelota                
            print "Coordenadas, Area: ", (x-w/2),(-(y-h/2)),int(dist)

            #Dibujamos una marca en el centro del objeto
            cv2.rectangle(imagen, (x-5, y-5), (x+5, y+5),(255,255,255), 18)
            #Marca el centro del area encontranda
            cv2.line(imagen,(0,y),(w,y),(255,0,0),2)        
            cv2.line(imagen,(x,0),(x,h),(255,0,0),2) 

        #Divide la imagen en cuatro cuadrantes
        cv2.line(imagen,(0,h/2),(w,h/2),(150,200,0),2)        
        cv2.line(imagen,(w/2,0),(w/2,h),(150,200,0),2)                   

        #Mostramos la imagen original con la marca del centro y la mascara
        cv2.imshow('mask', mask)
        cv2.imshow('Camara', imagen)
        tecla = cv2.waitKey(5) & 0xFF
        if tecla == ord('q'):
            break 
cv2.destroyAllWindows()