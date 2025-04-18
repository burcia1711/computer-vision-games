import cv2

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("RGB", rgb)
cv2.waitKey(0)
