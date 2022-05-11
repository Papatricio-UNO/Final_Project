# Project One: Updated Lab 9
# Added Features: GUI, mute button, on / off buttons for power and mute functions
import sys

from One_classes_copy import *


def main():
    app = QApplication(sys.argv)
    window = GUI()
    window.setFixedSize(599, 477)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
