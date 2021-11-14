import sys
import reader2
import ttts1
from ttts1 import Pz
from reader2 import Reader
import меню222
from check_db import *
from des import *
from regStr import *
import calc1
from calc1 import calc
from PyQt5.QtGui import QPixmap
from меню222 import Menu
import bloknot
from bloknot import Bloknot
import easygui
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout,
        QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)

SCREEN_SIZE = [771, 651]

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    def run2(self):
        self.int5 = Interface2()
        self.int5.show()


class Interface2(QtWidgets.QWidget, меню222.Menu):
    def __init__(self):
        super().__init__()
        self.ui = Menu()
        self.ui.setupUi(self)  # Инициализация GUI
        self.ui.pushButton.clicked.connect(self.OpenWin)
        self.ui.pushButton_3.clicked.connect(self.OpenWin2)
        self.ui.pushButton_2.clicked.connect(self.OpenWin3)
        self.ui.pushButton_4.clicked.connect(self.OpenWin4)
        self.ui.pushButton_5.clicked.connect(self.OpenPz)

    def OpenWin(self):
        self.pz = READER()
        self.pz.show()

    def OpenWin2(self):
        self.cl = calculator()
        self.cl.show()

    def OpenWin3(self):
        self.bl = VLOKNOT()
        self.bl.show()

    def OpenWin4(self):
        self.gf = VideoPlayer()
        self.gf.show()

    def OpenPz(self):
        self.pZ = PZ()
        self.pZ.show()


class PZ(QtWidgets.QWidget, ttts1.Pz):
    def __init__(self):
        super(PZ, self).__init__()
        self.ui = Pz()
        self.ui.setupUi(self)


class READER(QtWidgets.QWidget, reader2.Reader):
    def __init__(self):
        super(READER, self).__init__()
        self.ui = Reader()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.readerJPG)

    def readerJPG(self):
        input_file = easygui.fileopenbox(filetypes=["*.jpg"])
        self.pixmap1 = QPixmap(input_file)
        self.ui.label.resize(1141, 800)
        self.pixmap1 = self.pixmap1.scaled(1141, 800, QtCore.Qt.KeepAspectRatio)
        #pixmap4 = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.ui.label.setPixmap(self.pixmap1)


class VLOKNOT(QtWidgets.QWidget, bloknot.Bloknot):
    def __init__(self):
        super(VLOKNOT, self).__init__()
        self.ui = Bloknot()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.readR)

    def readR(self):
        input_file = easygui.fileopenbox(filetypes=["*.txt"])
        f = open(input_file, 'r', encoding='utf-8')
        a = f.read()
        self.ui.textEdit.setText(str(a))


class calculator(QtWidgets.QWidget, calc1.calc):
    def __init__(self):
        super(calculator, self).__init__()
        self.ui = calc()
        self.ui.setupUi(self)
        self.t = ""
        self.calcul = ""
        self.expr = ""
        self.ui.btn1.clicked.connect(self.run)
        self.ui.btn2.clicked.connect(self.run)
        self.ui.btn3.clicked.connect(self.run)
        self.ui.btn4.clicked.connect(self.run)
        self.ui.btn5.clicked.connect(self.run)
        self.ui.btn6.clicked.connect(self.run)
        self.ui.btn7.clicked.connect(self.run)
        self.ui.btn8.clicked.connect(self.run)
        self.ui.btn9.clicked.connect(self.run)
        self.ui.btn0.clicked.connect(self.run)
        self.ui.btn_plus.clicked.connect(self.calc)
        self.ui.btn_minus.clicked.connect(self.calc)
        self.ui.btn_mult.clicked.connect(self.calc)
        self.ui.btn_div.clicked.connect(self.calc)
        self.ui.btn_eq.clicked.connect(self.result)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)
        self.ui.btn_pow.clicked.connect(self.calc)
        self.data = ''
        self.data_eval = ''

    def run(self):
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.ui.table.display(self.data)
        elif self.data == '':
            self.ui.table.display(0)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.ui.table.display(self.data)

    def result(self):
        self.data = eval(self.data_eval)
        self.data_eval = str(self.data)
        self.ui.table.display(self.data)
        self.data = ''

    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.ui.table.display('')

    def sqrt(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()

    def calc(self):
        if self.data_eval:
            self.result()
            if self.data_eval[-1] not in ['+', '-', '/', '*', '^']:
                self.data_eval += self.sender().text()

            elif self.data >= 2147483647:
                signal.emit('Числа больше 2147483647 невозможно вывести!')
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval) - 1] + self.sender().text()
            self.data_eval = self.data_eval.replace('^', '**')


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()
        openButton = QPushButton("Открыть Gif файл")
        openButton.setToolTip("Открыть Gif файл или mp4")
        openButton.setStatusTip("Открыть Gif файл")
        openButton.setFixedHeight(24)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 8))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.openfile)
        openButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(149, 255, 224);")

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.start)
        self.playButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(149, 255, 224);")

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.pozeCh)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 7))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.stateChange)
        self.mediaPlayer.positionChanged.connect(self.posch)
        self.mediaPlayer.durationChanged.connect(self.shirina)
        self.mediaPlayer.error.connect(self.eror)
        self.statusBar.showMessage("Готово")
        self.statusBar.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(149, 255, 224);")

    def openfile(self):
        fileName = easygui.fileopenbox(filetypes=["*.mp4"])
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.start()

    def start(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def stateChange(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def posch(self, position):
        self.positionSlider.setValue(position)

    def shirina(self, duration):
        self.positionSlider.setRange(0, duration)

    def pozeCh(self, position):
        self.mediaPlayer.setPosition(position)

    def eror(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Ошибка: " + self.mediaPlayer.errorString())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
