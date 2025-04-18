import cv2

webcam=cv2.VideoCapture(1)

webcam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while True:
    control,frame=webcam.read()

    cv2.imshow("Webcam",frame)
    if cv2.waitKey(10)==27:
        break