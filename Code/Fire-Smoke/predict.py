from ultralytics import YOLO

model = YOLO('Model/final_model.pt')

model.predict(source='fire2.mp4', imgsz = 640, conf = 0.8, save = True)

# model.predict(source=0, imgsz = 640, conf = 0.6, save = True, show=True)