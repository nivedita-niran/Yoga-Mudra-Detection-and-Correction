import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 300
counter = 0

folder = "/Users/niveditaniran/Desktop/Sign language detection/Data/PrithviMudra"

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break
    
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        
        if w == 0 or h == 0:
            continue  # Skip to the next frame if the bounding box is invalid
        
        imgWhite = np.ones([imgSize, imgSize, 3], np.uint8) * 255
        imgCrop = img[y - offset: y + h + offset, x - offset: x + w + offset]
        
        if imgCrop.size == 0:
            continue  # Skip to the next frame if the cropped image is empty
        
        aspectratio = h / w
        
        if aspectratio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap: wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap: hCal + hGap, :] = imgResize

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite', imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)

cap.release()
cv2.destroyAllWindows()
