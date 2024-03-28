import serial
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

arduino = serial.Serial('COM3', 9600, timeout=1)

def send_to_arduino(data):
    arduino.write(data.encode())

results = model.predict(source=0, stream=True)

for result in results:
    for box in result.boxes:
        if box.cls == 0:
            send_to_arduino('detected')
        else:
            send_to_arduino('not_detected')

# Close the serial connection
arduino.close()