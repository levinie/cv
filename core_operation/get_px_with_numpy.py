import cv2

debug = True

img_path = "/home/levi/temp/cv/pic/beauty.jpg"
modify_path = "/home/levi/temp/cv/pic/beauty_modify.jpg"

img = cv2.imread(img_path)
# BGR
b = img.item(100, 100, 0)
g = img.item(100, 100, 1)
r = img.item(100, 100, 2)
print b, g, r

if debug:
    img.itemset((100, 100, 0), 255)
    img.itemset((100, 100, 1), 255)
    img.itemset((100, 100, 2), 255)

# write
cv2.imwrite(modify_path, img)