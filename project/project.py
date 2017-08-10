from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()
    
    def UAC(self):
        choice = QMessageBox.information(self, 'User Account Control',
                                     "Do you want to allow the program from an unkown publisher to make changes to this computer?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            return NoAccess(self) 
        else:
            pass

    def NoAccess(self):
        choice = QMessageBox.critical(self, 'Access Denied',
                                     """Access is denied. 

You require permissioin from the computer's administrator to make changes to this folder. 
                                        
Go to 'Settings' to manage user permission control.""" , QMessageBox.Ok)
        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass       
        

    def initGUI(self):
        self.setGeometry(0, 30, 1000, 600)
        self.setWindowTitle("version01")
        self.setObjectName("main")
        self.setStyleSheet("""
         QWidget#main {
             background-color: #191919
         }      
         """)


        self.powerbutton = QPushButton(self)
        self.powerbutton.resize(17, 17)
        self.powerbutton.setObjectName("powerbutton")
        self.powerbutton.setStyleSheet("""
            QPushButton#powerbutton {
            background-image: url('img/power.png');
            }
            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            } 
        """)
        self.powerbutton.move(10, 550)

        self.settings = QPushButton(self)
        self.settings.resize(17, 17)
        self.settings.setObjectName("settings")
        self.settings.setStyleSheet("""
            QPushButton#settings {
            background-image: url('img/settings2.png');
            }
            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            } 
        """)
        self.settings.move(10, 500)

        self.explorer = QPushButton(self)
        self.explorer.resize(17, 17)
        self.explorer.setObjectName("explorer")
        self.explorer.setStyleSheet("""
            QPushButton#explorer {
            background-image: url('img/explorer.png');
            }
            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            } 
        """)
        self.explorer.move(10, 450)

        self.header1 = QLabel(self)
        self.header1.setText("Leisure")
        self.header1.setStyleSheet("""
            QLabel {
            color: #D9D9D9
        }
        """)
        self.header1.move(205, 10) #x, y

        self.tile11 = QPushButton(self)
        self.tile11.resize(100, 100)
        self.tile11.setObjectName("netflix") #incorrect sRGB
        self.tile11.setStyleSheet("""
            QPushButton#netflix {
            background-image: url('img/netflix.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile11.move(200, 30)
        self.tile11.clicked.connect(self.UAC)

        self.tile12 = QPushButton(self)
        self.tile12.resize(100, 100)
        self.tile12.setObjectName("spotify")
        self.tile12.setStyleSheet("""
            QPushButton#spotify {
            background-image: url('img/spotify.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        self.tile12.move(310, 30)
        self.tile12.clicked.connect(self.NoAccess)

        self.tile13 = QPushButton(self)
        self.tile13.resize(100, 100)
        self.tile13.setObjectName("music") #incorrect sRGB
        self.tile13.setStyleSheet("""
            QPushButton#music {
            background-image: url('img/music.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }

        """)
        self.tile13.move(420, 30)

        self.header2 = QLabel(self)
        self.header2.setText("Office")
        self.header2.setStyleSheet("""
        QLabel {
        color: #D9D9D9
        }
        """)
        self.header2.move(205, 150)

        self.tile21 = QPushButton(self)
        self.tile21.resize(100, 100)
        self.tile21.setObjectName("word")
        self.tile21.setStyleSheet("""
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
        self.tile21.move(200, 170)

        self.tile22 = QPushButton(self)
        self.tile22.resize(100, 100)
        self.tile22.setObjectName("excel")
        self.tile22.setStyleSheet("""
            QPushButton#excel {
            background-image: url('img/excel.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile22.move(310, 170)

        self.tile23 = QPushButton(self)
        self.tile23.resize(100, 100)
        self.tile23.setObjectName("powerpoint")
        self.tile23.setStyleSheet("""
            QPushButton#powerpoint {
            background-image: url('img/powerpoint.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile23.move(420, 170)

        self.tile24 = QPushButton(self)
        self.tile24.resize(100, 100)
        self.tile24.setObjectName("sway")
        self.tile24.setStyleSheet("""
            QPushButton#sway {
            background-image: url('img/sway.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile24.move(200, 280)

        self.tile25 = QPushButton(self)
        self.tile25.resize(100, 100)
        self.tile25.setObjectName("reader")
        self.tile25.setStyleSheet("""
            QPushButton#reader {
            background-image: url('img/reader.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile25.move(310, 280)

        self.tile26 = QPushButton(self)
        self.tile26.resize(100, 100)
        self.tile26.setObjectName("onenote")
        self.tile26.setStyleSheet("""
            QPushButton#onenote {
            background-image: url('img/onenote.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }
        """)
        self.tile26.move(420, 280)



        self.header3 = QLabel(self)
        self.header3.setText("Creative")
        self.header3.setStyleSheet("""
        QLabel {
        color: #D9D9D9
        }
        """)
        self.header3.move(565, 10)

        self.tile31 = QPushButton(self)
        self.tile31.resize(100, 100)
        self.tile31.setObjectName("photoshop")
        self.tile31.setStyleSheet("""
            QPushButton#photoshop {
            background-image: url('img/photoshop.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }            
        """)
        self.tile31.move(560, 30)


        self.tile32 = QPushButton(self)
        self.tile32.resize(100, 100)
        self.tile32.setObjectName("bridge")
        self.tile32.setStyleSheet("""
            QPushButton#bridge {
            background-image: url('img/bridge.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }            
        """)
        self.tile32.move(670, 30)

        self.tile33 = QPushButton(self)
        self.tile33.resize(100, 100)
        self.tile33.setObjectName("cubase")
        self.tile33.setStyleSheet("""
            QPushButton#cubase {
            background-image: url('img/cubase.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }            
        """)
        self.tile33.move(780, 30)


        self.header4 = QLabel(self)
        self.header4.setText("System")
        self.header4.setStyleSheet("""
        QLabel {
        color: #D9D9D9
        }
        """)
        self.header4.move(565, 150)

        self.tile41 = QPushButton(self)
        self.tile41.resize(100, 100)
        self.tile41.setObjectName("settings")
        self.tile41.setStyleSheet("""
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
        self.tile41.move(560, 170)

        self.tile42 = QPushButton(self)
        self.tile42.resize(100, 100)
        self.tile42.setObjectName("explorer")
        self.tile42.setStyleSheet("""
            QPushButton#explorer {
            background-image: url('img/explorer3.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }            
        """)
        self.tile42.move(670, 170)

        self.tile43 = QPushButton(self)
        self.tile43.resize(100, 100)
        self.tile43.setObjectName("powershell")
        self.tile43.setStyleSheet("""
            QPushButton#powershell {
            background-image: url('img/powershell.png');
            }

            QPushButton {
            border: 1px #4682B4;
            }
            QPushButton:hover {
                border: 1px solid #D9D9D9;
            }            
        """)
        self.tile43.move(780, 170)


        self.listwidget = QListWidget(self)
        self.listwidget.addItem("A")
        self.listwidget.addItem("Access 2016")
        self.listwidget.addItem("Acrobat Reader DC")
        self.listwidget.addItem("Adobe Bridge CC")
        self.listwidget.addItem("Adobe Creative Cloud")
        self.listwidget.addItem("Adobe Media Endocer CC")
        self.listwidget.addItem("Adobe Photoshop CC")
        self.listwidget.addItem("Alarm & Clock")
        self.listwidget.addItem("Anaconda2")
        self.listwidget.addItem("Arduino")
        self.listwidget.addItem("Audacity")
        self.listwidget.addItem("Access 2016")
        self.listwidget.addItem("Acrobat Reader DC")
        self.listwidget.addItem("Adobe Bridge CC")
        self.listwidget.addItem("Adobe Creative Cloud")
        self.listwidget.addItem("Adobe Media Endocer CC")
        self.listwidget.addItem("Adobe Photoshop CC")
        self.listwidget.addItem("Alarm & Clock")
        self.listwidget.addItem("Anaconda2")
        self.listwidget.addItem("Arduino")
        self.listwidget.addItem("Audacity")
        self.listwidget.addItem("")
        self.listwidget.addItem("B")
        self.listwidget.addItem("Blender")
        self.listwidget.setStyleSheet("""
            QListWidget {
            font-family: "Monaco", "Andale Mono", monospace;
            font-size: 14px;
            color: #D9D9D9;
            background-color: #191919
            }

        """)
        #self.listwidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listwidget.resize(120, 400)
        self.listwidget.move(40, 30)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
