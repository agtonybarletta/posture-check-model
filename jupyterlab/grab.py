import cv2
import time
import datetime

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()

ret, frame = capture.read()
img_name = "opencv_frame_{}.png".format(datetime.datetime.now().isoformat())
cv2.imwrite(img_name, frame)
print("{} written!".format(img_counter))
start_time = time.time()
while True:
    ret, frame = capture.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #if time.time() - start_time >= 1: #<---- Check if 30 min passed
    if time.time() - start_time >= 900: #<---- Check if 30 min passed
        img_name = "opencv_frame_{}.png".format(datetime.datetime.now().isoformat())
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_counter))
        start_time = time.time()
    img_counter += 1
