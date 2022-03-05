import cv2
from sqlalchemy import true


# Read and display the original image
original = cv2.imread('me600.jpg')
cv2.imshow('Original', original)

# Convert to grayscale
greyscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# set initial values for the variables
blur_kernel = 3
blur_sigma = 1
sobel_dn = 1
sobel_kernel = 15

def draw():
    blurred = cv2.GaussianBlur(greyscale, (blur_kernel, blur_kernel), blur_sigma)
    sobelxy = cv2.Sobel(src=blurred, ddepth=cv2.CV_64F, dx=sobel_dn, dy=sobel_dn, ksize=sobel_kernel)

    cv2.imshow('Blurred', blurred)
    cv2.imshow('Sobel', sobelxy)
    cv2.waitKey(1)

# initial draw
draw()

# redraw the image with the new values
def on_blur_kernel_change(newval):
    global blur_kernel
    blur_kernel = newval
    # blur_kernel must be odd
    if blur_kernel % 2 == 0:
        blur_kernel -= 1
    # blur_kernel must be > 0
    if blur_kernel <= 0:
        blur_kernel = 1
    draw()

def on_blur_sigma_change(newval):
    global blur_sigma
    blur_sigma = newval
    draw()

def on_sobel_dn_change(newval):
    global sobel_dn
    sobel_dn = newval
    # sobel_dn must be > 0
    if sobel_dn <= 0:
        sobel_dn = 1
    draw()

def on_sobel_kernel_change(newval):
    global sobel_kernel
    sobel_kernel = newval
    # sobel_kernel must be odd
    if sobel_kernel % 2 == 0:
        sobel_kernel -= 1
    # sbel_kernel must be > 0
    if sobel_kernel <= 0:
        sobel_kernel = 1
    draw()

cv2.createTrackbar('blur_kernel', 'Blurred', blur_kernel, 100, on_blur_kernel_change)
cv2.createTrackbar('blur_sigma', 'Blurred', blur_sigma, 100, on_blur_sigma_change)
cv2.createTrackbar('sobel_dn', 'Sobel', sobel_dn, 100, on_sobel_dn_change)
cv2.createTrackbar('sobel_kernel', 'Sobel', sobel_kernel, 31, on_sobel_kernel_change)

while(True):
    cv2.waitKey(1)

