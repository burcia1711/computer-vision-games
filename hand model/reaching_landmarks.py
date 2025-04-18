import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(1)
hand_model = mp.solutions.hands

with hand_model.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6) as hands:
    while True:
        control, frame = webcam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        height, width, _ = frame.shape
        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                index_finger_point = handLandmark.landmark[8]
                x = int(index_finger_point.x * width)
                y = int(index_finger_point.y * height)
                cv2.circle(frame, (x, y), 10, (255, 0, 0), 10)
        cv2.imshow("Special Landmarks of Index Finger", frame)
        if cv2.waitKey(10) == 27:
            break
