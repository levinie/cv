import cv2
import numpy as np

img_path = "/home/levi/temp/cv/pic/beauty.jpg"

img = cv2.imread(img_path)
row, col = img.shape[:2]
M = np.float32([[1, 0, 50], [0, 1, 100]])
dst = cv2.warpAffine(img, M, (col, row))
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()