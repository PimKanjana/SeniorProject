import cv2
import numpy as np

input_image = cv2.imread("hair_cut.png")
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)


# Initiate ORB object
#orb = cv2.ORB()
orb = cv2.ORB_create()

# find the keypoints with ORB
keypoints = orb.detect(gray_image, None)
#print(keypoints)

# compute the descriptors with ORB
keypoints, descriptors = orb.compute(gray_image, keypoints)

print(keypoints)

print()

#print(descriptors[1])


# draw only the location of the keypoints without size or orientation
final_keypoints = cv2.drawKeypoints(input_image, keypoints, gray_image, color=(0,255,0), flags=0)

cv2.imshow('ORB keypoints', final_keypoints)
cv2.imwrite('key.png', final_keypoints)
cv2.waitKey()
