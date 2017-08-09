from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(10, 30, 600, 560)
        self.setWindowTitle("version01")
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
             background-color: darkgrey

         }
         """)
        self.tile1 = QPushButton(self)
        self.tile1.resize(100, 100)
        self.tile1.setObjectName("settings")
        self.tile1.setStyleSheet("""
            QPushButton#settings {
            background-image: url('img/settings.png');
            }
            
            QPushButton:hover {
                border: 2px solid white;
            }
        """)
        self.tile1.move(10, 10)

        self.tile2 = QPushButton(self)
        self.tile2.resize(100, 100)
        self.tile2.setObjectName("word")
        self.tile2.setStyleSheet("""
            QPushButton#word {
            background-image: url('img/word.png');
            }

            QPushButton:hover {
                border: 2px solid white;
            }
        """)
        self.tile2.move(120, 10)

        self.tile3 = QPushButton(self)
        self.tile3.resize(100, 100)
        self.tile3.setObjectName("atom")
        self.tile3.setStyleSheet("""
            QPushButton#atom {
            background-image: url('img/atom.png');
            }

            QPushButton:hover {
                border: 2px solid white;
            }
        """)
        self.tile3.move(230, 10)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
