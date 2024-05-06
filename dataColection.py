import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np 

cam = cv.VideoCapture(0)
deteksi = HandDetector(maxHands=1 )
imgSize = 300

offset = 20
while True:
    succes , img = cam.read()
    hands , img = deteksi.findHands(img)
    img = cv.flip(img , 1)
    cv.imshow("gambar", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand["bbox"]

        imgwhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset: y+h+offset, x-offset: x+w+offset]

        imgCropShape = imgCrop.shape 

        imgwhite[0:imgCropShape[0],0:imgCropShape[1]] = imgCrop

        cv.imshow("gambarterpotong",imgCrop)
        cv.imshow("gambarputih",imgwhite)

cam.release()
cv.destroyAllWindows()