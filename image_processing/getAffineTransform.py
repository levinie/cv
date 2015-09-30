import cv2
import numpy as np

img_path = "/home/levi/temp/cv/pic/affine.jpg"

img = cv2.imread(img_path)
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()