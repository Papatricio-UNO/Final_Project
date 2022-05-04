# Testing based off Lab 12 Documentation

from One_classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__ == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'

    def test_power_on(self):
        assert self.tv1.__str__ == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power_on()
        assert self.tv1.__str__ == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'

    def test_power_off(self):
        assert self.tv1.__str__ == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power_on()
        assert self.tv1.__str__ == 'TV status: Is on = True, Mute status: Is on = False, Channel = 0, Volume = 0'
        self.tv1.power_off()
        assert self.tv1.__str__ == 'TV status: Is on = False, Mute status: Is on = False, Channel = 0, Volume = 0'

