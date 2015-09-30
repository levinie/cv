import cv2
import numpy as np

bgr_green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(bgr_green, cv2.COLOR_BGR2HSV)
print hsv_green