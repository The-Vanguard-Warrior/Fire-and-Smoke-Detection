import cv2
import torch

import torchvision.transforms as transforms


vid = cv2.VideoCapture(0) 

while(True):
    ret, frame = vid.read()
    flipped_frame = cv2.flip(frame, 1)  # Flip the frame horizontally
    cv2.imshow('frame', flipped_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release()
cv2.destroyAllWindows()
def detect_fire(frame):
    # Implement your fire detection logic here
    # This function should return True if fire is detected in the frame, and False otherwise
    return False

vid = cv2.VideoCapture(0) 

while(True):
    ret, frame = vid.read()
    flipped_frame = cv2.flip(frame, 1)  # Flip the frame horizontally
    cv2.imshow('frame', flipped_frame)
    
    if detect_fire(flipped_frame):
        # Fire detected, take appropriate action
        # For example, you can send an alert or save the frame to a file
        print("Fire detected!")
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release()
cv2.destroyAllWindows()