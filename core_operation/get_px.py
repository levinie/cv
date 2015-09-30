import cv2

img_path = "/home/levi/temp/cv/pic/beauty.jpg"
modify_path = "/home/levi/temp/cv/pic/beauty_modify.jpg"

img = cv2.imread(img_path)
# print img
px = img[100, 100]
print px
# BGR
blue = img[100, 100, 0]
print blue
print img[100, 100, 1]
print img[100, 100, 2]

# modify
img[100, 100] = [255, 255, 255]
print img[100, 100]
cv2.imwrite(modify_path, img)