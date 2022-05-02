from PyQt5.QtWidgets import *
from One_view import Ui_ProjectOne_MainWindow


class Television(QMainWindow, Ui_ProjectOne_MainWindow):
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__mute = False

        # Power buttons
        self.PowerOn_btn.clicked.connect(self.power_on)
        self.PowerOff_btn.clicked.connect(self.power_off)

        # Channel buttons
        self.ChannelDown_btn.clicked.connect(self.channel_down)
        self.ChannelUp_btn.clicked.connect(self.channel_up)

        # Volume buttons
        self.VoluemDown_btn.clicked.connect(self.volume_down)
        self.VolumeUp_btn.clicked.connect(self.volume_up)

        # Mute buttons
        self.MuteOn_btn.clicked.connect(self.mute_on)
        self.MuteOff_btn.clicked.connect(self.mute_off)

    def power_on(self):
        self.__status = True
        self.PowerOn_label.setText(f'Power: {self.__status}')
        self.Channels_label.setText(f'Channel: {self.__channel}')
        self.Volume_label.setText(f'Volume: {self.__volume}')
        self.Mute_label.setText(f'Mute: {self.__mute}')

    def power_off(self):
        self.__status = False
        self.__mute = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.PowerOn_label.setText(f'Power: ')
        self.Channels_label.setText(f'Channel: ')
        self.Volume_label.setText(f'Volume: ')
        self.Mute_label.setText(f'Mute: ')

    def mute_on(self):
        if self.__status:
            self.__mute = True
            self.Mute_label.setText(f'Mute: {self.__mute}')

    def mute_off(self):
        if self.__status:
            self.__mute = False
            self.Mute_label.setText(f'Mute: {self.__mute}')

    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.Channels_label.setText(f'Channel: {self.__channel}')
            else:
                self.__channel = Television.MIN_CHANNEL
                self.Channels_label.setText(f'Channel: {self.__channel}')

    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.Channels_label.setText(f'Channel: {self.__channel}')
            else:
                self.__channel = Television.MAX_CHANNEL
                self.Channels_label.setText(f'Channel: {self.__channel}')

    def volume_up(self):
        if self.__status:
            if not self.__mute and self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
                self.Volume_label.setText(f'Volume: {self.__volume}')

    def volume_down(self):
        if self.__status:
            if not self.__mute and self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
                self.Volume_label.setText(f'Volume: {self.__volume}')

    def __str__(self):
        return f'TV status: Is on = {self.__status}, Mute status: Is on = {self.__mute},' \
               f'Channel = {self.__channel}, Volume = {self.__volume}'
