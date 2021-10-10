import time
import pyautogui
import cv2 as cv
import win32api
import win32con
import numpy as np
from matplotlib import pyplot as plt
from vision import Vision
import test
import clickmethouds
from WindowCapture import WindowCapture
from clickmethouds import *


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == '__main__':
    # initialize the WindowCapture class
    wincap = WindowCapture('RuneScape')

    # vision_empty = Vision('pics/EmptyInventory.png')

    while True:

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # points = vision_empty.find(screenshot, 0.7, 'points')
        x = test.testttt(screenshot)

        cv.imshow('Computer Vision', x)

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

print('Done.')
