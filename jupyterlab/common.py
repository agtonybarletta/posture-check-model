import cv2
import time
def getImageFromWebcam():

    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("test")
    
    img_name=""
    
    img_counter = 0
    start_time = time.time()
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
    
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(time.time())
            cv2.imwrite(img_name, frame)
            cv2.destroyAllWindows()
    
    cam.release()
    
    cv2.destroyAllWindows()
    return img_name
