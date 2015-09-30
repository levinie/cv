import cv2

img_path = "/home/levi/temp/cv/pic/beauty.jpg"

img = cv2.imread(img_path)
row, col = img.shape[:2]
M = cv2.getRotationMatrix2D((col / 2, row / 2), 90, 0.5)
dst = cv2.warpAffine(img, M, (col, row))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

