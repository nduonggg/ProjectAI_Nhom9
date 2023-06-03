import cv2
import numpy as np

loc_w = 25
loc_h = 30
location = cv2.imread(r'location_1.png')

location = cv2.resize(location, (loc_w,loc_h))
cv2.imwrite("location.png", location)

for i in range (location.shape[0]):
    for j in range (location.shape[1]):
        if( location[i,j,0] < 200 and location[i, j, 2] > 200):
           location[i,j] = (0, 255, 0)

cv2.imshow("Modified Image", location)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("destination.png", location)