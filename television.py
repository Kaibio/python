#This is a python file
#This python file will be called television.py

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
       self.__status = False
       self.__muted = False
       self.__volume = Television.MIN_VOLUME
       self.__channel = Television.MIN_CHANNEL

    def power(self):
        def get_status():
            return self.__status
        def set_status(power):
            self.__status = power

        if not get_status():
            set_status(True)
            get_status()
        else:
            set_status(False)
            get_status()

    def set_mute(self, sound):
        self.__muted = sound
    def mute(self):
        def set_mute(sound):
            self.__muted = sound
        if self.__status:
            if not self.__muted:
                set_mute(True)
                self.set_volume(Television.MIN_VOLUME)
                return self.__muted
            else:
                set_mute(False)
                self.set_volume(self.__volume + 1)
                return self.__muted

    def channel_up(self):
        def set_channel(num):
            self.__channel = num
        if self.__status:
            if self.__channel >= Television.MIN_CHANNEL or self.__channel <= Television.MAX_CHANNEL:
                set_channel(self.__channel + 1)
                if self.__channel > Television.MAX_CHANNEL:
                    set_channel(Television.MIN_CHANNEL)

    def channel_down(self):
        def set_channel(num):
            self.__channel = num

        if self.__status:
            if self.__channel >= Television.MIN_CHANNEL or self.__channel <= Television.MAX_CHANNEL:
                set_channel(self.__channel - 1)
                if self.__channel < Television.MIN_CHANNEL:
                    set_channel(Television.MAX_CHANNEL)

    def set_volume(self, num):
        self.__volume = num

    def volume_up(self):
        def set_volume(num):
            self.__volume = num

        if self.__status:
            if self.__volume >= Television.MIN_VOLUME or self.__volume <= Television.MAX_VOLUME:
                set_volume(self.__volume + 1)
                if self.__volume > Television.MAX_VOLUME:
                    set_volume(Television.MAX_VOLUME)
            if self.__muted:
                self.set_mute(False)
                set_volume(self.__volume + 1)
    def volume_down(self):
        def set_volume(num):
            self.__volume = num

        if self.__status:
            if self.__volume >= Television.MIN_VOLUME or self.__volume <= Television.MAX_VOLUME:
                set_volume(self.__volume - 1)
                if self.__volume < Television.MIN_VOLUME:
                    set_volume(Television.MIN_VOLUME)
            if self.__muted:
                self.set_mute(False)
                set_volume(self.__volume + 1)

    def __str__(self):
        return f'power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
