import cv2

img_path = "/home/levi/temp/cv/pic/beauty.jpg"
modify_path = "/home/levi/temp/cv/pic/beauty_modify.jpg"
gray_path = "/home/levi/temp/cv/pic/beauty_gray.jpg"

print "=== original image ==="
img = cv2.imread(img_path)
shape = img.shape
print shape
print img.size
print img.dtype

print "=== gray image ==="
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gray_path, gray)
gray_shape = gray.shape
print gray_shape
print gray.size
print gray.dtype