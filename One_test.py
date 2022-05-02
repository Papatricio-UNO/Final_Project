import unittest
from One_classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__ == 'TV status: Is on False, Mute status: Is on = False, Channel = 0, Volume = 0'


if __name__ == '__main__':
    unittest.main()
