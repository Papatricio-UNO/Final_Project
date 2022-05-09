from PyQt5.QtWidgets import *
from One_view import Ui_ProjectOne_MainWindow
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
        self.TV_screen.setText(f'TV status, TV volume, TV channel')

        def gui_tv_mute(self) -> None:
            self.tv.volume()
            self.TV_screen.setText(f'TV is on: {self.tv.status}')

        def gui_channel_up(self) -> None:
            self.tv.channel_up()
            self.TV_screen.setText(f'TV status, TV volume, TV channel')

        def gui_channel_down(self) -> None:
            pass

        def gui_volume_up(self) -> None:
            pass

        def gui_volume_down(self) -> None:
            pass