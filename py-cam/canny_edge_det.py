import cv2

# Read and display the original image
original = cv2.imread('me600.jpg')
cv2.imshow('Original', original)

# Convert to grayscale
greyscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# set initial values for the variables
blur_kernel = 3
blur_sigma = 1
cann_thrs1 = 100
cann_thrs2 = 200

def draw():
    blurred = cv2.GaussianBlur(greyscale, (blur_kernel, blur_kernel), blur_sigma)
    canny = cv2.Canny(image=blurred, threshold1=cann_thrs1, threshold2=cann_thrs2)

    cv2.imshow('Blurred', blurred)
    cv2.imshow('Canny', canny)
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

def on_cann_thrs1_change(newval):
    global cann_thrs1
    cann_thrs1 = newval
    draw()

def on_cann_thrs2_change(newval):
    global cann_thrs2
    cann_thrs2 = newval
    draw()

cv2.createTrackbar('blur_kernel', 'Blurred', blur_kernel, 100, on_blur_kernel_change)
cv2.createTrackbar('blur_sigma', 'Blurred', blur_sigma, 100, on_blur_sigma_change)
cv2.createTrackbar('cann_thrs1', 'Canny', cann_thrs1, 255, on_cann_thrs1_change)
cv2.createTrackbar('cann_thrs2', 'Canny', cann_thrs2, 255, on_cann_thrs2_change)

while(True):
    cv2.waitKey(1)

