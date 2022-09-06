from PySide2 import QtWidgets, QtGui
import os
#import server DON'T REMOVE


"""
This module contains the client() function that returns the path to the image.jpeg file.
Then the main() function opens the image.jpeg in a widget window.
"""

def client():
    path_to_image = os.getcwd() + '/image.jpeg'
    return path_to_image

def main():
    path = client()
    app = QtWidgets.QApplication([])
    label = QtWidgets.QLabel()
    label.setMinimumSize(100, 100)
    label.setPixmap(QtGui.QPixmap(path))
    label.show()
    app.exec_()

if __name__ == '__main__':
    main()
