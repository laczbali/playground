import subprocess
from time import sleep
import keyboard
import win32gui
import numpy as np
import cv2
from mss import mss
from PIL import Image
import pytesseract

def setup_dino():
    # launch a window
    command = "cmd /c start chrome --new-window"
    subprocess.Popen(command, shell=True)
    sleep(1)

    # navigate to dino (can't start there)
    keyboard.write('chrome://dino')
    keyboard.press_and_release('enter')
    sleep(1)

    # move to known location, with known size
    hwnd = win32gui.FindWindow(None, "chrome://dino/ - Google Chrome")
    win32gui.MoveWindow(hwnd, -7, 0, 500, 300, True) # -7 px offset, due to windows-things

def close_dino():
    # make sure focus is on the dino window
    hwnd = win32gui.FindWindow(None, "chrome://dino/ - Google Chrome")
    win32gui.SetForegroundWindow(hwnd)
    # close tab
    keyboard.press_and_release('ctrl+w')

def get_current_points(img):
    # THIS IS EXTREMELY SLOW
    text = pytesseract.image_to_string(img)
    number = 0
    try:
        number = int(text)
    except:
        pass
    return number

def run():
    TITLEBAR_OFFSET = 115
    bounding_box = {'top': TITLEBAR_OFFSET, 'left': 0, 'width': 500, 'height': 300-TITLEBAR_OFFSET-8} # 8px offset, due to windows-things

    while True:
        with mss() as sct:
            frame = np.array(sct.grab(bounding_box))

            frame_subset_points = frame[10:35, 420:]
            points = get_current_points(frame_subset_points)

            cv2.putText(
                frame,
                text=f"points {points}",
                org=(10, 30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 255, 255),
            )
            cv2.imshow('screen', frame)

            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                break

    close_dino()

def main():
    pytesseract.pytesseract.tesseract_cmd = "C:\\cygwin64\\bin\\tesseract.exe"
    setup_dino()
    run()

if __name__ == '__main__':
    main()