import cv2
import numpy as np

img_path = "../pic/beauty.jpg"

# Read image
im = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
# detector = cv2.SimpleBlobDetector()

# Detect blobs.
keypoints = detector.detect(im)

print len(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
# cv2.namedWindow("blob", cv2.WINDOW_NORMAL)
cv2.imshow("blob", im_with_keypoints)
# cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
