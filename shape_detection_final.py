import cv2
import numpy as np

file = '45.png'

# Opening and reading picture
img = cv2.imread(file, 0)
img2 = cv2.imread(file, 1)
frame = cv2.imread(file)

# Searching constants added to segregate colours
a = 6
b = 5
c = 11
d = 11
# e = 3

# Double filtering to remove the slightest noises
_, threshold = cv2.threshold(img, 85, 255, cv2.THRESH_BINARY)
blurred = cv2.GaussianBlur(threshold,(5,5),0)
_, threshold = cv2.threshold(blurred, 77, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# =============================================================================
# hsv1 = cv2.cvtColor(frame, 1)
# hsv2 = cv2.cvtColor(frame, 1)
# hsv3 = cv2.cvtColor(frame, 1)
# hsv4 = cv2.cvtColor(frame, 1)
# hsv5 = cv2.cvtColor(frame, 1)
# =============================================================================
bgr = cv2.cvtColor(frame, 1)

# define range of colours
lower_green = np.array([80,150,20])     # GREEN 
upper_green = np.array([180,220,70])

lower_orange = np.array([80,100,200])   # ORANGE 
upper_orange = np.array([120,180,255])

lower_blue = np.array([180,120,0])      # BLUE
upper_blue = np.array([255,180,30])      

lower_yellow = np.array([65,200,200])   # YELLLOW
upper_yellow = np.array([95,250,250])      

lower_red = np.array([60,40,150])       # RED
upper_red = np.array([100,80,244])      


# Threshold the HSV image to get only blue colors
mask_g = cv2.inRange(bgr, lower_green, upper_green)
mask_o = cv2.inRange(bgr, lower_orange, upper_orange)
mask_b = cv2.inRange(bgr, lower_blue, upper_blue)
mask_y = cv2.inRange(bgr, lower_yellow, upper_yellow)
mask_r = cv2.inRange(bgr, lower_red, upper_red)

# Bitwise-AND mask and original image
res_g = cv2.bitwise_and(frame,frame, mask= mask_g)
res_o = cv2.bitwise_and(frame,frame, mask= mask_o)
res_b = cv2.bitwise_and(frame,frame, mask= mask_b)
res_y = cv2.bitwise_and(frame,frame, mask= mask_y)
res_r = cv2.bitwise_and(frame,frame, mask= mask_r)

font = cv2.FONT_HERSHEY_COMPLEX

# Drawing shapes and displaying in respective files
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
#    print (len(approx))
    
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        shape = 'triangle'
        
    elif len(approx) == 4:
        shape = 'quadrilateral'
        
    elif len(approx) == 5:
        shape = 'pentagon'
        
    else:
        shape = 'circle'
        
    cv2.putText(img, shape, (x,y), font, 0.4, (255,255,255))


    if ((img2[y+a,x+b] >= [80,150,20]).all()):      # GREEN     
        if ((img2[y+a,x+b] <= [180,220,70]).all()):
            cv2.putText(res_g, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+a,x+b] >= [80,100,200]).all()):     # ORANGE 
        if ((img2[y+a,x+b] <= [120,180,255]).all()):
            cv2.putText(res_o, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+a,x+b] >= [180,120,0]).all()):      # BLUE
        if ((img2[y+a,x+b] <= [255,180,30]).all()):
            cv2.putText(res_b, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+8,x+5] >= [65,200,200]).all()):     # YELLOW
        if ((img2[y+8,x+5] <= [95,250,250]).all()):
            cv2.putText(res_y, shape, (x,y), font, 0.4, (255,255,255))               
            
    if ((img2[y+a,x+b] >= [60,40,150]).all()):      # RED
        if ((img2[y+a,x+b] <= [100,80,244]).all()):
            cv2.putText(res_r, shape, (x,y), font, 0.4, (255,255,255))

    # Left find
    
    if ((img2[y+c,x-d] >= [80,150,20]).all()):      # GREEN     
        if ((img2[y+c,x-d] <= [180,220,70]).all()):
            cv2.putText(res_g, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+c,x-d] >= [80,100,200]).all()):     # ORANGE 
        if ((img2[y+c,x-d] <= [120,180,255]).all()):
            cv2.putText(res_o, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+c,x-d] >= [180,120,0]).all()):      # BLUE
        if ((img2[y+c,x-d] <= [255,180,30]).all()):
            cv2.putText(res_b, shape, (x,y), font, 0.4, (255,255,255))
            
    if ((img2[y+c,x-d] >= [65,200,200]).all()):     # YELLOW
        if ((img2[y+c,x-d] <= [95,250,250]).all()):
            cv2.putText(res_y, shape, (x,y), font, 0.4, (255,255,255))               
            
    if ((img2[y+c,x-d] >= [60,40,150]).all()):      # RED
        if ((img2[y+c,x-d] <= [100,80,244]).all()):
            cv2.putText(res_r, shape, (x,y), font, 0.4, (255,255,255))
            
# =============================================================================
#     # Center
#             
#     if ((img2[y+e,x] >= [80,150,20]).all()):      # GREEN     
#         if ((img2[y+e,x] <= [180,220,70]).all()):
#             cv2.putText(res_g, shape, (x,y), font, 0.4, (255,255,255))
#             
#     if ((img2[y+e,x] >= [80,100,200]).all()):     # ORANGE 
#         if ((img2[y+e,x] <= [120,180,255]).all()):
#             cv2.putText(res_o, shape, (x,y), font, 0.4, (255,255,255))
#             
#     if ((img2[y+e,x] >= [180,120,0]).all()):      # BLUE
#         if ((img2[y+e,x] <= [255,180,30]).all()):
#             cv2.putText(res_b, shape, (x,y), font, 0.4, (255,255,255))
#             
#     if ((img2[y+e,x] >= [65,200,200]).all()):     # YELLOW
#         if ((img2[y+e,x] <= [95,250,250]).all()):
#             cv2.putText(res_y, shape, (x,y), font, 0.4, (255,255,255))               
#             
#     if ((img2[y+e,x] >= [60,40,150]).all()):      # RED
#         if ((img2[y+e,x] <= [100,80,244]).all()):
#             cv2.putText(res_r, shape, (x,y), font, 0.4, (255,255,255))
# 
# =============================================================================
#    print (y, x)


# =============================================================================
# cv2.imshow('original',img)
# cv2.imshow('threshold',threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

cv2.imshow('Image',frame)
cv2.imshow('Red coloured Objects',res_r)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image',frame)
cv2.imshow('Green coloured Objects',res_g)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image',frame)
cv2.imshow('Blue coloured Objects',res_b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image',frame)
cv2.imshow('Yellow coloured Objects',res_y)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image',frame)
cv2.imshow('Orange coloured Objects',res_o)
cv2.waitKey(0)
cv2.destroyAllWindows()
