"""
More info on QSlider: https://doc.qt.io/qt-5/qslider.html#details
"""

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QProgressBar, QLabel, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

class Sliders(QWidget):
    width = 800         #class variables
    height = 600

    def __init__(self):
        super(Sliders, self).__init__()
        self.initGUI()

    def initGUI(self):      #where the magic happens
        slider1 = QSlider(self)
        slider2 = QSlider(self)
        slider3 = QSlider(self)
        slider1.setOrientation(Qt.Horizontal)
        slider2.setOrientation(Qt.Horizontal)
        slider3.setOrientation(Qt.Horizontal)
        progress1 = QProgressBar(self)
        progress2 = QProgressBar(self)
        progress3 = QProgressBar(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)

        label1.setFrameStyle(QFrame.Box | QFrame.Raised)
        label1.setFont(QFont("Arial", 32, QFont.Bold))
        label1.setNum(0)

        label2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label2.setFont(QFont("Arial", 32, QFont.Bold))
        label2.setNum(0)

        label3.setFrameStyle(QFrame.Panel | QFrame.Plain)
        label3.setFont(QFont("Arial", 32, QFont.Bold))
        label3.setNum(0)

        # Connect signals
        slider1.valueChanged.connect(progress1.setValue)
        slider1.valueChanged.connect(label1.setNum)

        slider2.valueChanged.connect(progress2.setValue)
        slider2.valueChanged.connect(label2.setNum)

        slider3.valueChanged.connect(progress3.setValue)
        slider3.valueChanged.connect(label3.setNum)

        # Size and position everything
        slider1.setGeometry(20, 20, 400, 80)    #absolute positioning
        progress1.setGeometry(20, 100, 400, 20)
        label1.setGeometry(480, 40, 60, 60)

        slider2.setGeometry(20, 200, 400, 80)
        progress2.setGeometry(20, 280, 400, 20)
        label2.setGeometry(480, 220, 60, 60)

        slider3.setGeometry(20, 400, 400, 80)
        progress3.setGeometry(20, 480, 400, 20)
        label3.setGeometry(480, 420, 60, 60)

        self.setGeometry(0,25, self.width, self.height)
        self.setWindowTitle("sluts are just functions")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Sliders()
sys.exit(app.exec_())
