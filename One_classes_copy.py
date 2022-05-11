from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from One_Screen import Ui_ProjectOne_MainWindow
from One_Television import *


# To Do: Make new GUI file with one power btn and mute btn and updated UI with own TV SCREEN

class GUI(QMainWindow, Ui_ProjectOne_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.tv = Television()

        # Power buttons
        self.Power_btn.clicked.connect(self.gui_tv_power)

        # Channel buttons
        self.ChannelDown_btn.clicked.connect(self.gui_channel_down)
        self.ChannelUp_btn.clicked.connect(self.gui_channel_up)

        # Volume buttons
        self.VoluemDown_btn.clicked.connect(self.gui_volume_down)
        self.VolumeUp_btn.clicked.connect(self.gui_volume_up)

        # Mute buttons
        self.Mute_btn.clicked.connect(self.gui_tv_mute)

    def gui_tv_power(self) -> None:
        self.tv.power()
        if self.tv.get_status() is True:
            self.TV_screen.setPixmap(QtGui.QPixmap("imgs/static.png"))
        elif self.tv.get_status() is False:
            self.TV_screen.setPixmap(QtGui.QPixmap("imgs/black_screen.jpg"))
            self.Volume_display.setPixmap(QtGui.QPixmap("imgs/mute.png"))

    def gui_tv_mute(self) -> None:
        self.tv.volume()
        if self.tv.get_mute() is True:
            self.Volume_display.setPixmap(QtGui.QPixmap("imgs/mute.png"))
        elif self.tv.get_mute() is False:
            if self.tv.get_volume() == 0:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/mute.png"))
            elif self.tv.get_volume() == 1:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume01.png"))
            elif self.tv.get_volume() == 2:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume02.png"))

    def gui_channel_up(self) -> None:
        if self.tv.get_status() is True:
            self.tv.channel_up()
            if self.tv.get_channel() == 0:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/static.png"))
            elif self.tv.get_channel() == 1:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/news.png"))
            elif self.tv.get_channel() == 2:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/sports.png"))
            elif self.tv.get_channel() == 3:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/cartoons.png"))

    def gui_channel_down(self) -> None:
        if self.tv.get_status() is True:
            self.tv.channel_down()
            if self.tv.get_channel() == 0:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/static.png"))
            elif self.tv.get_channel() == 1:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/news.png"))
            elif self.tv.get_channel() == 2:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/sports.png"))
            elif self.tv.get_channel() == 3:
                self.TV_screen.setPixmap(QtGui.QPixmap("imgs/cartoons.png"))

    def gui_volume_up(self) -> None:
        if self.tv.get_status() is True:
            self.tv.volume_up()
            if self.tv.get_volume() == 0:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/mute.png"))
            elif self.tv.get_volume() == 1:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume01.png"))
            elif self.tv.get_volume() == 2:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume02.png"))

    def gui_volume_down(self) -> None:
        if self.tv.get_status() is True:
            self.tv.volume_down()
            if self.tv.get_volume() == 0:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/mute.png"))
            elif self.tv.get_volume() == 1:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume01.png"))
            elif self.tv.get_volume() == 2:
                self.Volume_display.setPixmap(QtGui.QPixmap("imgs/volume02.png"))
