import cv2

image = cv2.imread("image.jpg")
cv2.circle(image, (150, 150), 60, (0, 0, 255), 10)

cv2.imshow("Circle", image)
cv2.waitKey(0)
