import time

import win32api
import win32con


def reset_camera():
    # X: 1688 Y: 95 RGB: (126,  80,  29)
    click(1688, 95)


def smelting():
    time.sleep(1)
    click(1194, 756)
    time.sleep(3)
    click(907, 591)
    time.sleep(8)
    click(1079, 562)
    time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 1745 first horizontal
inventory = [(1745, 695)]
'''
click(inventory[0][0], inventory[0][1])
time.sleep(2)
click(inventory[0][0] + 45, inventory[0][1])
time.sleep(2)
click(inventory[0][0] + 45*2, inventory[0][1])
time.sleep(2)
click(inventory[0][0] + 45*3, inventory[0][1])
'''

# looping through each inventory item
# for i in range(0, 7):
#     for y in range(0, 4):
#         click(inventory[0][0] + 45*y, inventory[0][1] + 35*i)
#         time.sleep(2)
