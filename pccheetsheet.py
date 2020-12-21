import os
import sys
import time
from ctypes import windll

import pyautogui

from pc import PcBaseControl


class PcControlBaseSheet(PcBaseControl):
    """
    # 查阅keyname 参考 pyautogui/__init__.py:310  KEY_NAMES
    """

    def vol_up(self):
        self._click_key('volumeup')

    def vol_down(self):
        self._click_key('volumedown')

    def music_next(self):
        self._click_key('nexttrack')

    def music_last(self):
        self._click_key('prevtrack')

    def music_play_pause(self):
        self._click_key('playpause')

    def screen_off(self, sec=1):
        HWND_BROADCAST = 0xffff
        WM_SYSCOMMAND = 0x0112
        SC_MONITORPOWER = 0xF170
        MonitorPowerOff = 2
        SW_SHOW = 5

        def screenOff():
            windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND,
                                       SC_MONITORPOWER, MonitorPowerOff)

            shell32 = windll.LoadLibrary("shell32.dll")
            shell32.ShellExecuteW(None, 'open', 'rundll32.exe',
                                  'USER32', '', SW_SHOW)

        time.sleep(sec)
        screenOff()

    def screen_on(self):
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(currentMouseX, currentMouseY)

    def pc_shutdown(self, sec=5):
        if sys.platform == 'win32':
            os.system('shutdown -s -t {}'.format(sec))

    def pc_sleep(self, sec=5):
        if sys.platform == 'win32':
            time.sleep(sec)
            os.system('shutdown -h')

    @staticmethod
    def _click_key(key):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
