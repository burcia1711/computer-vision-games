import cv2

img = cv2.imread("image.jpg")

height, width, _ = img.shape

print("The height of our image:", height, " ", " The width of our image:", width, " ",
      "The channel number of our image:", _)
