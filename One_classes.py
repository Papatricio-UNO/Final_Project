from PyQt5.QtWidgets import *
from One_view import Ui_ProjectOne_MainWindow

class Television(QMainWindow, Ui_ProjectOne_MainWindow):
    def __init__(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.setupUi()

        self


# class Television:
#     MIN_CHANNEL = 0  # Minimum TV channel
#     MAX_CHANNEL = 3  # Maximum TV channel
#
#     MIN_VOLUME = 0  # Minimum TV volume
#     MAX_VOLUME = 2  # Maximum TV volume
#
#     def __init__(self):
#         self.__channel = Television.MIN_CHANNEL
#         self.__volume = Television.MIN_VOLUME
#         self.__status = False
#         self.__mute = False
#
#     def power(self):
#         if not self.__status:
#             self.__status = True
#         else:
#             self.__status = False
#
#     def mute(self):
#         if not self.__mute:
#             self.__mute = True
#         else:
#             self.__mute = False
#
#     def channel_up(self):
#         if self.__status:
#             if self.__channel < Television.MAX_CHANNEL:
#                 self.__channel += 1
#             else:
#                 self.__channel = Television.MIN_CHANNEL
#
#     def channel_down(self):
#         if self.__status:
#             if self.__channel > Television.MIN_CHANNEL:
#                 self.__channel -= 1
#             else:
#                 self.__channel = Television.MAX_CHANNEL
#
#     def volume_up(self):
#         if self.__mute:
#             if self.__status and self.__volume != Television.MAX_VOLUME:
#                 self.__volume += 1
#
#     def volume_down(self):
#         if self.__mute:
#             if self.__status and self.__volume != Television.MIN_VOLUME:
#                 self.__volume -= 1
#
#     def __str__(self):
#         return f'TV status: Is on = {self.__status}, ' \
#                f'Channel = {self.__channel}, Volume = {self.__volume}'
