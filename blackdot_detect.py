import cv2
import numpy as np

img = cv2.imread("hair_cut.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,180]) 

mask = cv2.inRange(img, lower_black, upper_black)
cv2.imshow("Mask",mask)
cv2.waitKey(0)
#cv2.destroyAllWindows()

_,cnts,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# area1 and area2 are the range of contour area, change accordingly
area1 = 1
area2 = 200
totalDots = []

# Count the total number of contours
for cnt in cnts:
	if area1 < cv2.contourArea(cnt) < area2:
		print(cv2.contourArea(cnt))
		totalDots.append(cnt)
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255,0), 2)
		center = (x,y)
		center2 = (int(x+(w/2)),int(y+(h/2)))
		#cv2.circle(mask,center,int(w/2),(255,255,255),2)
		cv2.circle(mask,center2,int(w/2),(255,255,255),2)
		#print ("center: ", center)
		print("center2: ",center2)
	
#text = "Total number of dots are: {}".format(len(totalDots))
#cv2.putText(mask, text, (50, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 255, 255), 2)

print("Total number of dots are:{}".format(len(totalDots)))
cv2.imshow("dot",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()



