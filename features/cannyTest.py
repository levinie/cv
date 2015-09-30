import cv2

img_path = "../pic/beauty.jpg"

img = cv2.imread(img_path, 0)
img = cv2.GaussianBlur(img, (3, 3), 0)
# canny = cv2.Canny(img, 0, 100)
canny = cv2.Canny(img, 100, 200)

cv2.namedWindow("canny", cv2.WINDOW_NORMAL)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()