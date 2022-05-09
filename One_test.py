# unittest based off Lab 11

import unittest
from One_classes import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tv1 = Television(QMainWindow, Ui_ProjectOne_MainWindow)

    def tearDown(self):
        del self.tv1

    def test_init(self):
        self.tv1.power_on()
        self.assertEqual(self.tv1.__str__(), 'TV status: Is on = True, Mute status: Is on = False,' 'Channel = 0, '
                                             'Volume = 0')


if __name__ == '__main__':
    unittest.main()
