class Television:
    """
    A class representing details for a television object
    """
    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 3  # Maximum TV volume

    def __init__(self) -> None:
        """""
        Constructor to create initial state of a TV object.  
        """""
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        self.__mute: bool = False

    def get_channel(self) -> int:
        return self.__channel

    def get_volume(self) -> int:
        return self.__volume

    def get_status(self) -> bool:
        return self.__status

    def get_mute(self) -> bool:
        return self.__mute

    def power(self) -> None:
        """
        Method to turn the television on or off
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def volume(self) -> None:
        """
        Method to turn the television on or off
        """
        if not self.__mute:
            self.__mute = True
        else:
            self.__mute = False

    def channel_up(self) -> None:
        """""
        Method to go up a television channel 
        """""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to go down a television channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase a television's volume
        """
        if self.__status:
            if not self.__mute and self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease a television's volume
        """
        if self.__status:
            if not self.__mute and self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to print the power status, channel, and volume
        """
        return f'TV status: Is on = {self.__status}, Mute status: Is on = {self.__mute}, ' \
               f'Channel = {self.__channel}, Volume = {self.__volume}'
