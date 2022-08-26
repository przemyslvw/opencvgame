from turtle import screensize
import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


while(True):

    screenshot = None 

    cv.imshow('Computer Vision', screenshot)

    # press q with the output window focused to exit
    # waits 1ms evey loop to key presses  
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
print('Done')