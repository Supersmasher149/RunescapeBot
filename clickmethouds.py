from main import click
import pyautogui

class ClickMethouds:

    def reset_camera(self):
        # X: 1688 Y: 95 RGB: (126,  80,  29)
        click(1688, 95)

    def new(self):
        pyautogui.moveTo(1745,685)
