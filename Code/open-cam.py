import cv2

vid = cv2.VideoCapture(0) 

while(True):
    ret, frame = vid.read()
    flipped_frame = cv2.flip(frame, 1)  # Flip the frame horizontally
    cv2.imshow('frame', flipped_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release()
cv2.destroyAllWindows()