from math import floor
import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat
import numpy as np

def to_ascii(img):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'. "
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 0.6
    font_color = (255, 255, 255)
    thickness = 1

    font_size = floor(15 * font_scale)
    reduced_width = floor(1280/font_size)
    reduced_height = floor(720/font_size)

    
    # downscale the image by 15 (each pixel will be represented by a 15x15 px char)
    small = cv2.resize(img, (reduced_width, reduced_height), interpolation=cv2.INTER_AREA)

    # invert colors
    small = cv2.bitwise_not(small)

    # create result image
    result = np.zeros((720, 1280), np.uint8)

    # go through each pixel in the input image
    for i in range(0, reduced_height):
        for j in range(0, reduced_width):
            # get the pixel value
            pixel = small[i, j]
            # get the char corresponding to the pixel value
            char_index = round(np.interp(pixel, [0, 255], [0, len(chars)-1]))
            char = chars[char_index]
            # put the char in the result image
            result = cv2.putText(result, char, (j*font_size, (i*font_size)+font_size), font, font_scale, font_color, thickness, cv2.LINE_AA)

    return result

# start capturing the physical camera
hw_cam = cv2.VideoCapture(0)

# set up output camera
cam = pyvirtualcam.Camera(width=1280, height=720, fps=20, device="OBS Virtual Camera", fmt=PixelFormat.GRAY)

while(True):

    # Capture the video frame (array of pixels, which are arrays of RGB values)
    ret, frame = hw_cam.read()
    
    # Convert to grayscale
    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur
    # blurred = cv2.GaussianBlur(greyscale, (3, 3), 1)

    # canny edge detection
    canny = cv2.Canny(image=greyscale, threshold1=20, threshold2=60)

    # resize the image to 1280x720
    resized = cv2.resize(canny, (1280, 720), interpolation=cv2.INTER_AREA)

    # convert to ascii art
    ascii = to_ascii(resized)
    # cv2.imshow('frame', ascii)
    # cv2.waitKey(1)
    
    # send the frame to the virtual camera
    cam.send(ascii)
    cam.sleep_until_next_frame()
    