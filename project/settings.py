import sys
from PyQt5.QtWidgets import *

class MyMainWindow(QWidget):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI() 

    def initUI(self):
        self.setGeometry(400, 100, 350, 400) #position x, postion y, breite, hoehe
        self.setWindowTitle('Settings')
        self.label1 = QLabel(self) 
        self.label1.setText("User Administration Management")
        self.label1.setStyleSheet("""
        QLabel {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 14px;
            color: #D9D9D9;
            background-color: #191919
        }
        """)

        self.box = QLabel(self)
        self.box.setMargin(50)
        box.setStyleSheet("""
        QLabel {
            border: 2px solid black
        }
        """)
        
        self.full = QCheckBox(self)
        self.full.setText("Full")
        self.full.setStyleSheet("""
        QCheckBox {
	        font-family: "Monaco", "Andale Mono", monospace;
	    }
        QCheckBox::indicator {
            font-family: "Monaco", "Andale Mono", monospace;
        }   
             
        """)
        self.full.move(200, 200)


        # self.layout = QHBoxLayout()
        # layout.addWidget(self.full)
        # self.read = QCheckBox("Read")
        # self.layout.addWidget(QCheckBox("Full Control"))
        # self.layout.addWidget(QCheckBox("Read"))
        # self.layout.addWidget(QCheckBox("Write"))
        # self.layout.addWidget(QCheckBox("Change"))
        # self.setLayout(self.layout)



        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec_())