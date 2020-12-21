class PcBaseControl(object):

    def vol_up(self):
        raise NotImplementedError

    def vol_down(self):
        raise NotImplementedError

    def music_next(self):
        raise NotImplementedError

    def music_last(self):
        raise NotImplementedError

    def music_play_pause(self):
        raise NotImplementedError

    def screen_off(self, sec):
        raise NotImplementedError

    def screen_on(self):
        raise NotImplementedError

    def pc_shutdown(self, sec):
        raise NotImplementedError

    def pc_sleep(self, sec):
        raise NotImplementedError
