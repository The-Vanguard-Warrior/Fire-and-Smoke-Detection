import cv2
import time

cap = cv2.VideoCapture('video_input.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) #xem toc do thuc the khi qua video
print(fps) # xem toc do , o day la 25 anh tren giay
wait_time = 1000/fps # dong nhat don vi

while True:
    pre_time = time.time() # thoi gian truoc khi chay thuat toan
    img = cap.read()[1]
    img = cv2.medianBlur(img,3) # Gia xu co thuat toan xen vao
    cv2.imshow('Video', img)
    delta_time = (time.time() - pre_time)*1000 # thoi gian sau khi chay thuat toan
    print(delta_time)
    if delta_time > wait_time: #do thoi gian delta_time co the am, nên su dung ham if
        delay_time = 1
    else:
        delay_time = wait_time - delta_time # thoi gian delay
    if cv2.waitKey(int(delay_time)) == ord('q'):
        break
cv2.destroyAllWindows()