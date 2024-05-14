from ultralytics import YOLO
import cv2
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO("best.pt")

video_path = "backwards.mp4"
cap = cv2.VideoCapture(1)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model.track(frame, persist=True,conf=0.5)
        annotated_frame = results[0].plot()
        cv2.imshow("Fall Tracking", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()