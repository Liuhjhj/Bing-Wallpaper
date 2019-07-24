# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp, QDesktopWidget
import getpass,os
import DownloadMoudle


class Ui_BingWallpaper(object):
    def setupUi(self, BingWallpaper):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        BingWallpaper.setObjectName("BingWallpaper")
        BingWallpaper.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(current_dir+"/Icon.jpg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        BingWallpaper.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BingWallpaper)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.read = QtWidgets.QLabel(BingWallpaper)
        self.read.setObjectName("read")
        self.verticalLayout.addWidget(self.read)
        self.read_2 = QtWidgets.QLabel(BingWallpaper)
        self.read_2.setObjectName("read_2")
        self.verticalLayout.addWidget(self.read_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.download_file_label = QtWidgets.QLabel(BingWallpaper)
        self.download_file_label.setObjectName("download_file_label")
        self.horizontalLayout_2.addWidget(self.download_file_label)
        self.file = QtWidgets.QLineEdit(BingWallpaper)
        self.file.setToolTip("")
        self.file.setWhatsThis("")
        self.file.setAccessibleDescription("")
        self.file.setInputMask("")
        self.file.setCursorPosition(0)
        self.file.setObjectName("file")
        self.horizontalLayout_2.addWidget(self.file)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.download_num_label = QtWidgets.QLabel(BingWallpaper)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.download_num_label.sizePolicy().hasHeightForWidth())
        self.download_num_label.setSizePolicy(sizePolicy)
        self.download_num_label.setObjectName("download_num_label")
        self.horizontalLayout.addWidget(self.download_num_label)
        self.num = QtWidgets.QLineEdit(BingWallpaper)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num.sizePolicy().hasHeightForWidth())
        self.num.setSizePolicy(sizePolicy)
        self.num.setObjectName("num")
        self.horizontalLayout.addWidget(self.num)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.download_button = QtWidgets.QPushButton(BingWallpaper)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_3.addWidget(self.download_button)
        self.exit_button = QtWidgets.QPushButton(BingWallpaper)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_3.addWidget(self.exit_button)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.textEdit = QtWidgets.QTextEdit(BingWallpaper)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.center()
        self.download_button.clicked.connect(self.download_wallpaper)
        self.exit_button.clicked.connect(qApp.quit)
        self.retranslateUi(BingWallpaper)
        QtCore.QMetaObject.connectSlotsByName(BingWallpaper)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = BingWallpaper.geometry()
        BingWallpaper.move((screen.width() - size.width()) / 2,
                           (screen.height() - size.height()) / 2)

    def retranslateUi(self, BingWallpaper):
        _translate = QtCore.QCoreApplication.translate
        BingWallpaper.setWindowTitle(
            _translate(
                "BingWallpaper",
                "BingWallpaper"))
        self.read.setText(_translate("BingWallpaper", "Bing壁纸下载软件"))
        self.read_2.setText(_translate("BingWallpaper", "可下载今日的Bing壁纸"))
        self.download_file_label.setText(_translate("BingWallpaper", "下载目录:"))
        self.file.setPlaceholderText(
            _translate(
                "BingWallpaper",
                "/home/" + getpass.getuser() + "/Downloads"))
        self.download_num_label.setText(
            _translate("BingWallpaper", "下载数量(1~7):"))
        self.num.setPlaceholderText(_translate("BingWallpaper", "1"))
        self.download_button.setText(_translate("BingWallpaper", "开始下载"))
        self.exit_button.setText(_translate("BingWallpaper", "退出"))

    def download_wallpaper(self):
        self.textEdit.clear()
        self.num.clear()
        if self.file.text() == '':
            self.file.setText('/home/' + getpass.getuser() + '/Downloads/')
        if self.num.text() == '':
            istp = DownloadMoudle.download_start()
        else:
            istp = DownloadMoudle.download_start(
                self.num.text())

        if istp == '' or istp == 'DownloadFail':
            print(istp)
            self.textEdit.setText('下载失败')
            return
        for wallpaper in istp:
            print('wallpaper=', wallpaper)
            url = wallpaper[7:-1]
            filename = url[11:32]
            filepath = self.file.text() + filename + '.jpg'
            download_url = 'https://www.bing.com' + url
            self.textEdit.append('开始下载' + filepath)
            err = DownloadMoudle.download_file(
                filepath, download_url)
            if err == 'Error':
                self.textEdit.append('下载出错,请检查下载路径是否正确')
                return
        self.textEdit.append('已完成下载任务')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BingWallpaper = QtWidgets.QWidget()
    ui = Ui_BingWallpaper()
    ui.setupUi(BingWallpaper)
    BingWallpaper.show()
    sys.exit(app.exec_())
