import numpy
import cv2
import matplotlib

cap = cv2.VideoCapture('http://10.45.70.129:2109/video')

while cap.isOpened(): 
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
cap.release()
cv2.destroyAllWindows()