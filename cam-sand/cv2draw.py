import cv2
import numpy as np

coord_x = 100
coord_y = 100

while(True):
    # create empty frame
    frame = np.zeros((720, 1280, 3), np.uint8)

    # draw a circle
    cv2.circle(
        img=frame,
        center=(coord_x, coord_y),
        radius=50,
        color=(255, 255, 255),
        thickness=-1
    )

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
