from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.header1 = QLabel(self)
        self.header1.setText("Fun")
        self.header1.setStyleSheet("""
        QLabel {
        color: #D9D9D9
        }
        """)
        #self.header1.move(15, 10)

        self.header2 = QLabel(self)
        self.header2.setText("Fun")
        self.header2.setStyleSheet("""
        QLabel {
        color: #D9D9D9
        }
        """)
        #self.header2.move(15, 10)

        self.tile1 = QPushButton(self)
        self.tile1.resize(100, 100)
        self.tile1.setObjectName("settings")
        self.tile1.setStyleSheet("""
            QPushButton#settings {
            background-image: url('img/settings.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        #self.tile1.move(10, 30)

        self.tile2 = QPushButton(self)
        self.tile2.resize(100, 100)
        self.tile2.setObjectName("word")
        self.tile2.setStyleSheet("""
            QPushButton#word {
            background-image: url('img/word.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        #self.tile2.move(120, 30)

        self.tile3 = QPushButton(self)
        self.tile3.resize(100, 100)
        self.tile3.setObjectName("atom")
        self.tile3.setStyleSheet("""
            QPushButton#atom {
            background-image: url('img/atom.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        #self.tile3.move(230, 30)

        self.tile4 = QPushButton(self)
        self.tile4.resize(100, 100)
        self.tile4.setObjectName("slack")
        self.tile4.setStyleSheet("""
            QPushButton#slack {
            background-image: url('img/slack.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        #self.tile4.move(340, 30)

        grid = QGridLayout()
        grid.addWidget(self.tile1, 0, 0, 1, 1)
        grid.addWidget(self.tile2, 0, 1, 1, 1)
        grid.addWidget(self.tile3, 0, 2, 1, 1)
        grid.addWidget(self.header1, 1, 2, 1, 1)
        grid.addWidget(self.header2, 2, 2, 1, 1)

        mainwidget = QWidget()
        mainwidget.setLayout(grid)
        mainwidget.setObjectName("main")
        mainwidget.setStyleSheet("""
         QWidget#main {
             background-color: #191919
         }
         """)
        self.setCentralWidget(mainwidget)
        self.setWindowTitle("version01")
        self.setGeometry(0, 30, 800, 800)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
