
# https://www.youtube.com/watch?v=eLTLtUVuuy4

# importing openCV, numpy
import cv2
import numpy as np
import matplotlib.pyplot as plt
# getting the image file usig imread(srcImage)
image = cv2.imread('test_image.jpg')

# imshow('nameOfWindow',src_image_Object) : shows the image, but closes instantly
cv2.imshow('result', image)

# waitKey(milliSec) : waits for specific time for the user to view the content
# if 0 : then press enter for the code to proceed
cv2.waitKey(0)

# copying the image object to lae_image object
lane_image = np.copy(image)

# converting lane_image the color to greyscale
#gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

''' GaussianBlur(B/W_image, kernel, deviation) : blurs the lane_image to reduce 
		the amount of noise in the greyscale converted image.
		kernel is matrix i.e (rows, columns) whose color values whould be averaged around the image
		'''
#blur = cv2.GaussianBlur(gray, (5, 5), 0)
#cv2.imshow("result", blur)
# cv2.waitKey(0)

''' Canny(blur_image, lowThreshold, highThreshold) : function that automatically 
	multiplies the kernel in (5,5) and produces a gradient
	 if the edge of two pixel is higher than highThreshold, it's accepted as edge pixel; (the intensity will be high)
	 if the edge of two pixel is lower than lowThreshold, it's rejected; (the intensity will be low)
	 use 1:2 or 1:3 ratio for low and high threshold
'''
#canny = cv2.Canny(blur, 50, 150)
#cv2.imshow("result", canny)
# cv2.waitKey(0)

# putting these in a function


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

