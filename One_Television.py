class Television:
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2

    def __init__(self):
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        self.__mute: bool = False

    def get_channel(self):
        return self.__channel

    def get_volume(self):
        return self.__volume

    def get_status(self):
        return self.__status

    def get_mute(self):
        return self.__mute

    def set_channel(self, channel):
        if 0 <= self.__channel <= Television.MAX_CHANNEL:
            self.__channel = channel

    def set_volume(self, volume):
        if 0 <= self.__volume <= Television.MAX_VOLUME:
            self.__volume = volume

    def set_status(self, status):
        self.__status = status

    def set_mute(self, mute):
        self.__mute = mute

    def power_on(self) -> None:
        self.__status: bool = True

    def power_off(self) -> None:
        self.__status: bool = False
        self.__mute: bool = False

    def mute_on(self) -> None:
        if self.__status:
            self.__mute: bool = True

    def mute_off(self) -> None:
        if self.__status:
            self.__mute: bool = False

    def channel_up(self) -> None:
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        if self.__status:
            if not self.__mute and self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        if self.__status:
            if not self.__mute and self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        return f'TV status: Is on = {self.__status}, Mute status: Is on = {self.__mute},' \
               f'Channel = {self.__channel}, Volume = {self.__volume}'
