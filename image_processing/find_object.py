import cv2
import numpy as np

img_path = "/home/levi/temp/cv/pic/5.jpeg"
mask_path = "/home/levi/temp/cv/pic/mask.jpg"
ret_path = "/home/levi/temp/cv/pic/find_object.jpg"

img = cv2.imread(img_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([110, 50, 50])
upper = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
ret = cv2.bitwise_and(img, img, mask = mask)
cv2.imwrite(mask_path, mask)
cv2.imwrite(ret_path, ret)
