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
        def get_mute():
            return self.__muted

        def set_mute(sound):
            self.__muted = sound

        if not get_mute():
            set_mute(True)
            get_mute()
        else:
            set_mute(False)
            get_mute()

    def channel_up(self):
        def set_channel(num):
            self.__channel = num
        if self.__channel >= Television.MIN_CHANNEL or self.__channel <= Television.MAX_CHANNEL:
            set_channel(self.__channel + 1)
            if self.__channel > Television.MAX_CHANNEL:
                set_channel(Television.MIN_CHANNEL)

    def channel_down(self):
        pass
    def volume_up(self):
        pass
    def volume_down(self):
        pass
    def __str__(self):
        return f'power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

tv_1 = Television()
tv_1.channel_up()
print(tv_1)
tv_1.channel_up()
print(tv_1)
tv_1.channel_up()
print(tv_1)
tv_1.channel_up()
print(tv_1)