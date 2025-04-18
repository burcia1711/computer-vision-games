import cv2
import numpy as np

image = cv2.imread("image2.jpg")
rot90 = np.rot90(image)

cv2.imshow("Rotated", rot90)
cv2.imshow("Original", image)
cv2.waitKey(0)
