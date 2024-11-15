# Importing Libraries
import cv2 
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2) 

# Start capturing video from webcam 
cap = cv2.VideoCapture(0) 
keyboard = Controller()

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

detector = HandDetector(maxHands=2, detectionCon=0.8)

while True: 
    # Read video frame by frame 
    success, img = cap.read() 

    # Flip the image(frame) 
    img = cv2.flip(img, 1) 

    # Convert BGR image to RGB image 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    hand = detector.findHands(img, draw=False) 
    # Process the RGB image 
    results = hands.process(imgRGB) 
    
    if len(hand[0]): 
        
          # Taking the landmarks of hand 
        lmlist = hand[0][0]  
        if lmlist: 
            
              # Find how many fingers are up 
            # This function return list 
            fingerup = detector.fingersUp(lmlist)   
              
            # Change image based on  
            # different-different conditions 
            
            if fingerup[0] == 1:
                keyboard.press(Key.left)
            if fingerup[0] == 0:
                keyboard.release(Key.left)
                
            if fingerup[1] == 1:
                 keyboard.press(Key.up)
                 keyboard.release(Key.down)
            if fingerup[1] == 0:
                 keyboard.release(Key.up)
                 keyboard.press(Key.down)
                 
            if fingerup[2] == 1:
                keyboard.press(Key.right)
            if fingerup[2] == 0:
                keyboard.release(Key.right)
                
            if fingerup[0] == 1:
                keyboard.press(Key.left)
            if fingerup[0] == 0:
                keyboard.release(Key.left)
                
            if fingerup == [0, 0, 0, 0, 0]: 
                keyboard.release(Key.space)
                keyboard.press(Key.down)
            
            if fingerup == [1, 1, 1, 1, 1]: 
                keyboard.press(Key.space)
                keyboard.release(Key.down)
                
            if fingerup == [0, 1, 0, 0, 1]:
                keyboard.release(Key.up)
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                keyboard.press(Key.down)
                keyboard.release(Key.down)
            
# =============================================================================
#             if fingerup == [0, 1, 0, 0, 0] or fingerup == [1, 1, 1, 0, 0]: 
#                 keyboard.press(Key.up)
#             
#             if fingerup == [0, 1, 1, 0, 0]: 
#                 keyboard.pressed(Key.up)
#                 keyboard.press(Key.right)
#             
#             if fingerup == [1, 1, 0, 0, 0]: 
#                  keyboard.pressed(Key.up)                
#                  keyboard.press(Key.left)
#             
#             if fingerup == [1, 1, 1, 1, 1]: 
#                  keyboard.pressed(Key.up)
#                  keyboard.press(Key.space)
#             
#             if fingerup == [0, 0, 0, 0, 0]: 
#                  keyboard.press(Key.down)
#             
#             keyboard.release(Key.up)
#             keyboard.release(Key.down)
#             keyboard.release(Key.right)
#             keyboard.release(Key.left)
#             keyboard.release(Key.space)
# =============================================================================
    

# Get hand landmarks
#    if results.multi_hand_landmarks:
#        for hand_landmarks in results.multi_hand_landmarks:
#            lmlist = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
#            fingers_up = detector.fingersUp(lmlist)
#               
#            if fingers_up == [0, 1, 0, 0, 0]: 
#                keyboard.press('w')
#            elif fingers_up == [0, 1, 1, 0, 0]: 
#                with keyboard.pressed('w'):
#                    keyboard.press('d')
#            elif fingers_up == [1, 1, 0, 0, 0]: 
#                with keyboard.pressed('w'):
#                    keyboard.press('a')
#            elif fingers_up == [1, 1, 1, 1, 1]: 
#                with keyboard.pressed('w'):
#                    keyboard.press(Key.space)
#            elif fingers_up == [0, 0, 0, 0, 0]: 
#                keyboard.press('s') 
    
    cv2.imshow('Camera', img) 
    if cv2.waitKey(1) & 0xff == ord('p'):
        break
cap.release() 
cv2.destroyAllWindows() 