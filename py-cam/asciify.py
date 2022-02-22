from math import floor
import cv2
import numpy as np

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'. "

font = cv2.FONT_HERSHEY_PLAIN
font_scale = 0.5
font_color = (255, 255, 255)
thickness = 1

font_size = floor(15 * font_scale)
reduced_size = floor(600/font_size)

# Read and display the original image
original = cv2.imread('me600.jpg')

# downscale the image by 15 (each pixel will be represented by a 15x15 px char)
small = cv2.resize(original, (reduced_size, reduced_size), interpolation=cv2.INTER_AREA)

# convert to greyscale
greyscale = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

# create result image
result = np.zeros((600, 600), np.uint8)

# go through each pixel in the greyscale image
for i in range(0, reduced_size):
    for j in range(0, reduced_size):
        # get the pixel value
        pixel = greyscale[i, j]
        # get the char corresponding to the pixel value
        char = chars[round(np.interp(pixel, [0, 255], [0, len(chars)-1]))]
        # put the char in the result image
        result = cv2.putText(result, char, (j*font_size, (i*font_size)+font_size), font, font_scale, font_color, thickness, cv2.LINE_AA)

# display resulting image
cv2.imshow('Original', result)
cv2.waitKey(0)