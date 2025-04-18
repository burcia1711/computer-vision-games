import cv2

webcam = cv2.VideoCapture(1)

while True:
    control, frame = webcam.read()

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(10) == 27:
        break
