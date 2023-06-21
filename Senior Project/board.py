# Imports
import os
import platform
from turtle import color
import numpy as np
import time
from datetime import datetime
import cv2
import mediapipe as mp

# folderPath = "Option Header"
# myList = os.listdir(folderPath)
# print(myList)
# overList = []

# img_header = cv2.imread('black.jpg', 1)


boardWidth = 500
boardHeight = 500
board = np.zeros((boardHeight, boardWidth, 1), dtype=np.uint8)
board.fill(255)

xp = 0
yp = 0

start = (100, 50)
end = (125, 80)


def move(pointerX, pointerY, image):
    cv2.circle(image, (pointerX, pointerY), 2, (255, 0, 0), 30)



def draw():
    cv2.circle(img, (pointerX, pointerY), 2, (0, 0, 255), 10)


def erase():
    # cv2.rectangle(img, start, end, (255, 0, 255), 23)
    # 255, 250, 255

    cv2.circle(img, (pointX, pointY), 2, (255, 0, 255), 23)


# def er():
    # cv2.rectangle(board, start, end, (255, 255, 255), 30)

    # cv2.circle(board, (pointX, pointY), 2, (255, 255, 255), 23)


def save(time, currentBoard):
    if platform.system() == "Linux":
        print("Linux directory not set yet!")
    else:
        dir = 'C:/Users/Richard Sinclair/Documents/test'
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = os.path.join(dir, '%s.png' % time).replace("\\", "/")
    cv2.imwrite(path,  cv2.flip(currentBoard, 1))
    print(path)


# Video capture
cap = cv2.VideoCapture(0)

# Variables
mpHands = mp.solutions.hands
hands = mpHands.Hands()
handDraw = mp.solutions.drawing_utils
pointerX = 0
pointerY = 0
fingerY = [0] * 21
fingersUp = [0] * 5
previousTime = 0
currentTime = 0

pointX = 0
pointY = 0
saveTime = datetime.now()
saveString = saveTime.strftime("Saved_%m_%d_%y_%I_%M%p")
# Video loop and processing
while True:

    # converts color & prints
    detected, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Getting various information about the landmarks on the hand
    if results.multi_hand_landmarks:

        for landmarks in results.multi_hand_landmarks:
            #handDraw.draw_landmarks(img, landmarks, mpHands.HAND_CONNECTIONS)
            for ids, lm in enumerate(landmarks.landmark):
                height, width, center = img.shape
                centerX, centerY = int(lm.x * width), int(lm.y * height)

                fingerY[ids] = centerY

                # Fingertip recognition logic (May need tweaked. Thumb recognition is a little iffy)
                if ids == 8:
                    pointerX = centerX
                    pointerY = centerY

                if fingerY[6] > fingerY[8]:
                    fingersUp[0] = 1
                    #xp == 0 and yp == 0
                    #print("Index finger up!")
                elif fingerY[6] < fingerY[8]:
                    fingersUp[0] = 0
                    #print ("Index finger down!")
                if fingerY[10] > fingerY[12]:
                    fingersUp[1] = 1
                    #print("Middle finger up!")
                elif fingerY[10] < fingerY[12]:
                    fingersUp[1] = 0
                    #print ("Middle finger down!")
                if fingerY[14] > fingerY[16]:
                    fingersUp[2] = 1
                    #print("Ring finger up!")
                elif fingerY[14] < fingerY[16]:
                    fingersUp[2] = 0
                    #print ("Ring finger down!")
                if fingerY[18] > fingerY[20]:
                    fingersUp[3] = 1
                    #print("Pinky finger up!")
                elif fingerY[18] < fingerY[20]:
                    fingersUp[3] = 0
                    #print ("Pinky finger down!")
                if fingerY[2] - fingerY[4] > 75:
                    fingersUp[4] = 1
                    #print ("Thumb out!")
                else:
                    fingersUp[4] = 0
                    #print("Thumb in!")

                # Case statement to match gestures to functions (Functions may still be tweaked or added)
                match fingersUp:

                    case [0, 0, 0, 0, 0]:
                        print("No gestures detected")
                    case [1, 0, 0, 0, 0]:
                        #print("Draw function!")
                        xp, yp = pointerX, pointerY
                        cv2.line(img, (xp, yp), (pointerX, pointerY), draw(), thickness=35)
                        cv2.line(board, (xp, yp), (pointerX, pointerY), draw(), thickness=13)
                        xp, yp = pointerX, pointerY

                    case [1, 1, 0, 0, 0]:
                        #print("Movement function")
                        move(pointerX, pointerY, flip)
                    case [1, 1, 1, 1, 0]:
                        print("Erase  function!")
                        cv2.line(board, (xp, yp), (pointX, pointY), (255, 250, 255), thickness=35)
                        xp, yp = pointX, pointY
                    case [1, 1, 1, 0, 0]:
                        #print("Save function!")
                        save(saveString, board)

    # Code to compute FPS and show on screen
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 3)
    #flipped = cv2.flip(img, 1)
    flip = cv2.flip(board, 1)
    # Show contents of frame
    cv2.imshow("Frame", img)
    cv2.imshow('board', flip)
    cv2.waitKey(1)
