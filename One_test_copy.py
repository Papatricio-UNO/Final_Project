# unittest based off Lab 11

import unittest
from One_classes_copy import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv1 = Television()

    def tearDown(self):
        del self.tv1

    def test_init(self):
        self.tv1.power_on()
        self.assertEqual(self.tv1.__str__(), 'TV status: Is on = True, Mute status: Is on = False,' 'Channel = 0, '
                                             'Volume = 0')

    def test_power_off(self):
        self.tv1.power_on()
        self.assertEqual(self.tv1.__str__(), 'TV status: Is on = True, Mute status: Is on = False,' 'Channel = 0, '
                                             'Volume = 0')
        self.tv1.power_off()
        self.assertEqual(self.tv1.__str__(), 'TV status: Is on = False, Mute status: Is on = False,' 'Channel = 0, '
                                             'Volume = 0')

if __name__ == '__main__':
    unittest.main()
