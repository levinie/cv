import cv2

img_path = "/home/levi/temp/cv/pic/beauty.jpg"
new_path = "/home/levi/temp/cv/pic/beauty_move_block.jpg"

img = cv2.imread(img_path)
block = img[500:600, 350:450]
img[0:100, 700:800] = block
cv2.imwrite(new_path, img)