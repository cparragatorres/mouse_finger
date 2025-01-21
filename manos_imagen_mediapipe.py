import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:

    image = cv2.imread("img/img6.jpg")
    height, width, _ = image.shape
    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    # HANDEDNESS
    # clasifica las manos detectadas
    print("Handedness: ", results.multi_handedness)
    # HAND LANDMARKS
    # print("Hand Landmarks: ", results.multi_hand_landmarks)     #ubica los 21 puntos de coordenada de cada mano

    if results.multi_hand_landmarks is not None:
        # ---------------------------------------
        # Dibujando los puntos y sus conexiones con mediapipe
        '''
        for hand_landmarks in results.multi_hand_landmarks:
            #print(hand_landmarks)
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,255),thickness=2,circle_radius=6),
                mp_drawing.DrawingSpec(color=(51,57,255),thickness=2))
        #---------------------------------------
        '''
        '''
        #---------------------------------------    
        #Accediendo a los puntos clave, de acuerdo a su NOMBRE
        for hand_landmarks in results.multi_hand_landmarks:
            x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width)
            y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
            
            x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width)
            y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height)
            
            x3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
            y3 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)
            
            x4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * width)
            y4 = int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * height)
            
            x5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width)
            y5 = int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height)
            
            cv2.circle(image,(x1,y1),3,(255,0,0),2)
            cv2.circle(image,(x2,y2),3,(255,0,0),2)
            cv2.circle(image,(x3,y3),3,(255,0,0),2)
            cv2.circle(image,(x4,y4),3,(255,0,0),2)
            cv2.circle(image,(x5,y5),3,(255,0,0),2)
        #---------------------------------------
        '''

        # ---------------------------------------
        # Accediendo a los puntos clave, de acuerdo a su INDICE
        index = [4, 8, 12, 16, 20]
        for hand_landmarks in results.multi_hand_landmarks:
            for (i, points) in enumerate(hand_landmarks.landmark):
                if i in index:
                    x = int(points.x * width)
                    y = int(points.y * height)
                    cv2.circle(image, (x, y), 3, (255, 0, 0), 2)

        # ---------------------------------------

    image = cv2.flip(image, 1)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
