import cv2

img_path = "../pic/beauty.jpg"
gray_path = "../out/pic/gray_path.jpg"
hsv_path = "../out/pic/hsv_path.jpg"

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gray_path, gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite(hsv_path, hsv)
