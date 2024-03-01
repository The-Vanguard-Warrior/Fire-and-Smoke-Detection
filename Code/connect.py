import cv2

cap = cv2.VideoCapture(1)

while True:
    rate,frame = cap.read()
    
    cv2.imshow('web_cam',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()