from turtle import screensize
import cv2 as cv
import numpy as np
import os
from PIL import ImageGrab

os.chdir(os.path.dirname(os.path.abspath(__file__)))


while(True):

    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    # press q with the output window focused to exit
    # waits 1ms evey loop to key presses  
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done')