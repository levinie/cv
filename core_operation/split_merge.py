import cv2

img_path = "/home/levi/temp/cv/pic/beauty.jpg"
new_path = "/home/levi/temp/cv/pic/beauty_split.jpg"

img = cv2.imread(img_path)
# img[:, :, 0] = 0
# img[:, :, 1] = 0
img[:, :, 2] = 0
cv2.imwrite(new_path, img)