# importing the OpenCV library
import cv2
# reading the image
img = cv2.imread(r"MYtwiter.png")
# using the QRCodeDetector() function
dectector = cv2.QRCodeDetector()
# using the detectAndDecode() function
val,b,c= dectector.detectAndDecode(img)
# printing the value
print("Information:", val)

