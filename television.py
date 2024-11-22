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
    def mute(self):
        def get_status():
            return self.__muted

        def set_status(sound):
            self.__muted = sound

        if not get_status():
            set_status(True)
            get_status()
        else:
            set_status(False)
            get_status()
    def channel_up(self):
        pass
    def channel_down(self):
        pass
    def volume_up(self):
        pass
    def volume_down(self):
        pass
    def __str__(self):
        return f'power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
