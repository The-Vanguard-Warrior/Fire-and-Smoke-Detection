from ultralytics import YOLO

model = YOLO('fire.pt')

model.predict(source='99.jpg', imgsz = 640, conf = 0.6, save = True)

# model.predict(source=0, imgsz = 640, conf = 0.6, save = True, show=True)