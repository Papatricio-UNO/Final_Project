# Project One: Updated Lab 9
# Features: GUI, mute button

from One_classes import *


def main():
    app = QApplication([])
    window = Television()
    window.show()
    window.setFixedSize(250, 300)
    app.exec_()


if __name__ == '__main__':
    main()
