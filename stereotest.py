import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('caml.jpg',0)
imgR = cv2.imread('camr.jpg',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
#stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,16, 15)

disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
