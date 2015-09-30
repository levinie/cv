import cv2
import numpy as np

img_path = "/home/levi/temp/cv/pic/perspective.jpg"

img = cv2.imread(img_path)
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()