import cv2

img_path1 = "/home/levi/temp/cv/pic/beauty.jpg"
img_path2 = "/home/levi/temp/cv/pic/7.jpg"
img_path_add = "/home/levi/temp/cv/pic/img_add.jpg"

img1_src = cv2.imread(img_path1)
img1 = img1_src[0:720, 0:482]
img2 = cv2.imread(img_path2)
img_add = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
cv2.imwrite(img_path_add, img_add)



