import cv2
import numpy as np

file = 'shapes.jpg'

img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file, 1)
_, threshold = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow('threshold',threshold)

frame = cv2.imread(file)

# Convert BGR to HSV
hsv1 = cv2.cvtColor(frame, 1)
hsv2 = cv2.cvtColor(frame, 1)
hsv3 = cv2.cvtColor(frame, 1)

# define range of blue color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([255,20,20])
lower_green = np.array([0,0,0])
upper_green = np.array([20,255,20])
lower_red = np.array([0,0,0])
upper_red = np.array([20,20,255])

# Threshold the HSV image to get only blue colors
mask_b = cv2.inRange(hsv1, lower_blue, upper_blue)
mask_g = cv2.inRange(hsv2, lower_green, upper_green)
mask_r = cv2.inRange(hsv3, lower_red, upper_red)

# Bitwise-AND mask and original image
res_b = cv2.bitwise_and(frame,frame, mask= mask_b)
res_g = cv2.bitwise_and(frame,frame, mask= mask_g)
res_r = cv2.bitwise_and(frame,frame, mask= mask_r)

font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    print (len(cnt))
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        shape = 'triangle'
        
    elif len(approx) == 4:
        shape = 'rectangle'
        
    elif len(approx) == 5:
        shape = 'pentagon'

    elif len(approx) == 6:
        shape = 'hexagon'              
      
    else:
        shape = 'circle'
        
    #cv2.putText(img2, shape, (x,y), font, 1, (255,0,0))
    cv2.putText(img, shape, (x,y), font, 1, (255,255,255))
    
    if ((img2[y+8,x+2] <= [255,20,20]).all()):  
        cv2.putText(res_b, shape, (x,y), font, 1, (255,0,0))
    
    if ((img2[y+8,x+2] <= [20,255,20]).all()):
        cv2.putText(res_g, shape, (x,y), font, 1, (0,255,0))

    if ((img2[y+8,x+2] <= [20,20,255]).all()):
        cv2.putText(res_r, shape, (x,y), font, 1, (0,0,255))
    
    
# cv2.imshow('shapes', img)
cv2.imshow('blue',res_b)
cv2.imshow('green',res_g)
cv2.imshow('red',res_r)

cv2.waitKey(0)
cv2.destroyAllWindows()