# Project One: Updated Lab 9
# Added Features: GUI, mute button, on / off buttons for power and mute functions

from One_classes_copy import *


def main():
    app = QApplication([])
    window = GUI()
    window.show()
    window.setFixedSize(599, 477)
    app.exec_()


if __name__ == '__main__':
    main()
