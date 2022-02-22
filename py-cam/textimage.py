from math import floor
import cv2
import numpy as np

image = np.zeros((720,1280), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
font_scale = 0.5
font_color = (255, 255, 255)
thickness = 1

font_size = floor(15 * font_scale)

# fill image with '0' chars
# at font_scale=1, one char is roughly 15x15 pixels
#   which means 85x48 chars, at 1280x720 resolution ()

for i in range(0, floor(720/font_size)):
    for j in range(0, floor(1280/font_size)):
        image = cv2.putText(
            image,
            '0',
            (j*font_size, (i*font_size)+font_size),
            font,
            font_scale,
            font_color,
            thickness,
            cv2.LINE_AA
        )


cv2.imshow('image', image)
cv2.waitKey(0)
