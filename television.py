#This is a python file
#This python file will be called television.py

class Television:
    """
    This is a class that represents a television's basic functions
    Power - Turn it off and on
    Volume - Up, down, and mute
    Channel - Up and down
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        These are the defalt settings of the television
        """
       self.__status = False
       self.__muted = False
       self.__volume = Television.MIN_VOLUME
       self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns the tele off and on
        """
        def get_status():
            """
            Returns the current status of the tele
            """
            return self.__status
        def set_status(power):
            """
            Pulls the power status from the base function
            """
            self.__status = power

        if not get_status():
            """
            If power is set to false, set it to true - turn the tv on
            """
            set_status(True)
            get_status()
        else:
            """
            If power is set to true, set it to false - turn the tv off
            """
            If it is set 
            set_status(False)
            get_status()

    def set_mute(self, sound):
        """
        Pull the status of the television sound
        Paramaters:
        sound (bool): The mute status to set.
        """
        self.__muted = sound
    def mute(self):
        """
        Changes the status of the muted tele

        """
        def set_mute(sound):
            """
            Pulling the status of the sound, from initial set
            """
            self.__muted = sound
        if self.__status:
            
            if not self.__muted:
                """
                If tv isn't muted - mute it 
                """
                set_mute(True)
                self.set_volume(Television.MIN_VOLUME)
                return self.__muted
            else:
                """
                If tv is muted - turn it up by one
                """
                set_mute(False)
                self.set_volume(self.__volume + 1)
                return self.__muted

    def channel_up(self):
        """
        Turns channel up by one
        """
        def set_channel(num):
            """
            Pulls the intial value
            """
            self.__channel = num
        if self.__status:
            if self.__channel >= Television.MIN_CHANNEL or self.__channel <= Television.MAX_CHANNEL:
                """
                Turns the channel up by one
                """
                set_channel(self.__channel + 1)
                if self.__channel > Television.MAX_CHANNEL:
                    """
                    If it is more than the max, then it circles back around 
                    to the first channel
                    """
                    set_channel(Television.MIN_CHANNEL)

    def channel_down(self):
        """
        Turns channel down by one
        """
        def set_channel(num):
            """
            Pulls the intial channel
            """
            self.__channel = num

        if self.__status:
            if self.__channel >= Television.MIN_CHANNEL or self.__channel <= Television.MAX_CHANNEL:
                """
                Decreases channel by one
                """
                set_channel(self.__channel - 1)
                if self.__channel < Television.MIN_CHANNEL:
                    """
                    If channel is less then min channel then it circles back to the max channel
                    """"
                    set_channel(Television.MAX_CHANNEL)

    def set_volume(self, num):
        """
        determines the volume of the tele
        Parameters:
        num (int): The volume level
        """
        self.__volume = num

    def volume_up(self):
        """
        turns up volume by one
        """
        def set_volume(num):
            """
            Pulls intial volume
            """
            self.__volume = num

        if self.__status:
            if self.__volume >= Television.MIN_VOLUME or self.__volume <= Television.MAX_VOLUME:
                """
                increases volume by one
                """"
                set_volume(self.__volume + 1)
                if self.__volume > Television.MAX_VOLUME:
                    """
                    If it is more than the max volume
                    set volume to the max
                    """
                    set_volume(Television.MAX_VOLUME)
            if self.__muted:
                """
                If it is muted, increase volume by one
                """
                self.set_mute(False)
                set_volume(self.__volume + 1)
    def volume_down(self):
        """
        decreases volume by one
        """
        def set_volume(num):
            """
            Pulls intial volume
            """
            self.__volume = num

        if self.__status:
            if self.__volume >= Television.MIN_VOLUME or self.__volume <= Television.MAX_VOLUME:
                """
                decreases volume by one
                """"
                set_volume(self.__volume - 1)
                if self.__volume < Television.MIN_VOLUME:
                    """
                    if volume reaches the min volume
                    set volume to min volume
                    """
                    set_volume(Television.MIN_VOLUME)
            if self.__muted:
                """
                if volume is muted
                increase volume by one
                """
                self.set_mute(False)
                set_volume(self.__volume + 1)

    def __str__(self):
        """
        Returns current status about the tele power, channel, and the volume
        """
        return f'power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
