import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


#########################
wCam, hCam = 640, 480
#########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)


while True:
    #Paso 1. Encontar los puntos de referencia de las manos
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPostion(img)
    
    #Paso 2. Consigue la punta de los dedos índice y medio
    #Paso 3. Verificar qué dedos están arriba
    #Paso 4. Solo dedo índice: modo de movimiento, y si esta en movimiento debemos convertir las coordenadas en valores
    #Paso 5. Convertir coordenadas
    #Paso 6. Suavizar valores (al estar nervioso)
    #Paso 7. Mover el ratón
    #Paso 8. Tanto el dedo Índice como el dedo Medio están arriba: Modo de clic
    #Paso 9. Encuentra la distancia entre los dedos
    #Paso 10. Haga clic con el mouse si la distancia es corta
    #Paso 11. fps-velocidad por fotogramas
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    
    #Paso 12. Display-Mostrar
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
