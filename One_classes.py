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

        # Power button
        self.power_button.clicked.connect(self.power)

        # Channel buttons
        self.ChannelDown_btn.clicked.connect(self.channel_down)
        self.ChannelUp_btn.clicked.connect(self.channel_up)

        # Volume buttons
        self.VoluemDown_btn.clicked.connect(self.volume_down)
        self.VolumeUp_btn.clicked.connect(self.volume_up)

        # Mute button
        self.Mute_btn.clicked.connect(self.mute)

    def power(self):
        if self.power_button.isChecked():
            if not self.__status:
                self.__status = True
                self.power_label.setText('On')
            else:
                self.__status = False
                self.power_label.setText('Off')

    def mute(self):
        if self.Mute_btn.isChecked():
            self.__mute = True
        else:
            self.__mute = False

    def channel_up(self):
        if self.ChannelUp_btn.isChecked():
            if self.__status:
                if self.__channel < Television.MAX_CHANNEL:
                    self.__channel += 1
                    self.Channels_label.setText(f'Channel: {self.__channel}')
                else:
                    self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.ChannelDown_btn.isChecked():
            if self.__status:
                if self.__channel > Television.MIN_CHANNEL:
                    self.__channel -= 1
                    self.Channels_label.setText(f'Channel: {self.__channel}')
                else:
                    self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.VolumeUp_btn.isChecked():
            if self.__status:
                if self.__mute and self.__volume != Television.MAX_VOLUME:
                    self.volume += 1
                    self.Volume_label.sextText(f'Volume: {self.__volume}')

    def volume_down(self):
        if self.VoluemDown_btn.isChecked():
            if self.__status:
                if self.__mute and self.__volume != Television.MIN_VOLUME:
                    self.volume -= 1
                    self.Volume_label.sextText(f'Volume: {self.__volume}')
