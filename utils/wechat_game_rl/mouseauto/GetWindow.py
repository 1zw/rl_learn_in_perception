import win32gui
import win32con
from PyQt5.QtWidgets import QApplication
import numpy as np
import os,time
WORK_DIR_PATH = os.getcwd()
class GetWindow():
    def __init__(self,except_name = "跃动方块"):
        self.dir      = os.path.join(os.path.split(os.path.realpath(__file__))[0],'click_img')
        self.path     = os.path.join(self.dir,'Img.jpg')
        self.title    = except_name
        self.hwnd     = None
        self.everlook = False
        self.window_width = 440
        self.window_height = 790
    def get_handle(self):
        '''
        Open the game interface and display the window directly in front
        '''
        hwnd_list  = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwnd_list)
        for hwnd in hwnd_list:
            # print(win32gui.GetWindowText(hwnd))
            if win32gui.GetWindowText(hwnd) == self.title:
                self.hwnd = hwnd
                print("Get the {} window handle as {}".format(self.title,hwnd))
                win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE) 
                win32gui.SetForegroundWindow(self.hwnd) # Brings the window to the front
                time.sleep(1.0) 
                self.everlook = True
                return True
        print("Could not get the handle to the game window, please ensure the game is started")
        return False
    def capture(self,mode = 0, path = None):
        raise NotImplementedError
        