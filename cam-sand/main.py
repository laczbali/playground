import cv2

# start capturing the physical camera
hw_cam = cv2.VideoCapture(0)

while(True):
    ret, frame = hw_cam.read()

    resized = cv2.resize(frame, (40, 40), interpolation=cv2.INTER_AREA)
    grey = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image=grey, threshold1=100, threshold2=120)

    upscaled = cv2.resize(canny, (400, 400), interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', upscaled)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break