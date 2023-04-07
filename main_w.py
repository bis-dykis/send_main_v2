# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 802)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 571, 91))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 40, 48, 21))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 40, 61, 21))
        self.id_edit = QLineEdit(self.groupBox)
        self.id_edit.setObjectName(u"id_edit")
        self.id_edit.setGeometry(QRect(80, 35, 151, 31))
        self.pass_edit = QLineEdit(self.groupBox)
        self.pass_edit.setObjectName(u"pass_edit")
        self.pass_edit.setGeometry(QRect(350, 34, 191, 31))
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 200, 171, 16))
        self.list_edit = QLineEdit(self.centralwidget)
        self.list_edit.setObjectName(u"list_edit")
        self.list_edit.setGeometry(QRect(40, 230, 430, 30))
        self.list_btn = QPushButton(self.centralwidget)
        self.list_btn.setObjectName(u"list_btn")
        self.list_btn.setGeometry(QRect(500, 230, 70, 30))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 280, 161, 16))
        self.attach_edit = QLineEdit(self.centralwidget)
        self.attach_edit.setObjectName(u"attach_edit")
        self.attach_edit.setGeometry(QRect(40, 310, 430, 30))
        self.attach_btn = QPushButton(self.centralwidget)
        self.attach_btn.setObjectName(u"attach_btn")
        self.attach_btn.setGeometry(QRect(500, 310, 70, 30))
        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setEnabled(True)
        self.send_btn.setGeometry(QRect(240, 700, 141, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 390, 48, 16))
        self.subject_edit = QLineEdit(self.centralwidget)
        self.subject_edit.setObjectName(u"subject_edit")
        self.subject_edit.setGeometry(QRect(40, 420, 531, 31))
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font.setPointSize(10)
        self.subject_edit.setFont(font)
        self.body_edit = QTextEdit(self.centralwidget)
        self.body_edit.setObjectName(u"body_edit")
        self.body_edit.setGeometry(QRect(40, 490, 531, 191))
        self.body_edit.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 470, 48, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 350, 291, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 150, 71, 16))
        self.sender_edit = QLineEdit(self.centralwidget)
        self.sender_edit.setObjectName(u"sender_edit")
        self.sender_edit.setGeometry(QRect(110, 140, 161, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\ud558\uc774\uc6cd\uc2a4 \uacc4\uc815", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc774\uba54\uc77c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud328\uc2a4\uc6cc\ub4dc", None))
        self.id_edit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uac70\ub798\ucc98 \uba54\uc77c \ub9ac\uc2a4\ud2b8 (\uc5d1\uc140\ud30c\uc77c)", None))
        self.list_btn.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\ucca8\ubd80\ud30c\uc77c(PDF + Excel) \uacbd\ub85c", None))
        self.attach_btn.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"\uba54\uc77c \uc804\uc1a1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ubaa9", None))
        self.subject_edit.setText(QCoreApplication.translate("MainWindow", u"10\uc6d4 \uac70\ub798 \ub0b4\uc5ed\uc744 \ubcf4\ub0b4 \ub4dc\ub9bd\ub2c8\ub2e4.", None))
        self.body_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub098\ub214\uace0\ub515'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt;\">\uc548\ub155\ud558\uc138\uc694. \uc720\ub77c\uc774\ud504\ud30c\uc774\ub0b8\uc15c\uc785\ub2c8\ub2e4. &lt;br&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9"
                        "pt;\">&lt;br&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt;\">%s \uae08\uc6d4 \uac70\ub798 \ub0b4\uc5ed\uc744 \ubcf4\ub0b4 \ub4dc\ub9ac\ub2c8 \ud655\uc778 \ubd80\ud0c1 \ub4dc\ub9bd\ub2c8\ub2e4.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt;\"><br /></p></body"
                        "></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub0b4\uc6a9", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u203b \uc8fc\uc758 \uc5c5\uccb4\uba85\uc774 \ud30c\uc77c\uba85\uacfc \uac19\uc544\uc57c \ud568. ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\ub0b4\ub294 \uc0ac\ub78c", None))
        self.sender_edit.setText(QCoreApplication.translate("MainWindow", u"toursafe@bis.co.kr", None))
    # retranslateUi

