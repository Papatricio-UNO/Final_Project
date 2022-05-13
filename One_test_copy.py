# unittest based off Lab 11

import unittest
from One_classes_copy import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv1 = Television()

    def tearDown(self):
        del self.tv1

    def test_init(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'

    def test_power_off(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 1, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 2, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 3, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 3, Volume = 0'
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.channel_down()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 2, Volume = 0'
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 1, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 1'
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 3'

    def test_volume_down(self):
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 1'

    def test_mute(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.volume()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'TV status: Is on = True, Mute status: Is on = True, Channel = 0, Volume = 0'


if __name__ == '__main__':
    unittest.main()
