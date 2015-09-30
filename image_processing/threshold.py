import cv2
import numpy as np

img_path = "/home/levi/temp/cv/pic/threshold.png"

# img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
print img.shape

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(len(titles)):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()