import cv2

img_path1 = "/home/levi/temp/cv/pic/beauty.jpg"
img_path2 = "/home/levi/temp/cv/pic/7.jpg"
img_path_add = "/home/levi/temp/cv/pic/img_add.jpg"

img1 = cv2.imread(img_path1)
img2 = cv2.imread(img_path2)
img1_size = img1.shape
img2_resize = cv2.resize(img2, (img1_size[1], img1_size[0]))
img_add = cv2.addWeighted(img1, 0.8, img2_resize, 0.2, 0)
cv2.imwrite(img_path_add, img_add)

