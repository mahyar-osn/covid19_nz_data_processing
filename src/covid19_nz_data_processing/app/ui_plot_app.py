# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plot_app.ui'
#
# Created: Fri Apr 17 15:47:38 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 439)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("../../../../../../../brain/codes/python_packages/PyQt-Image-Viewer/icons/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.export_2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_2.sizePolicy().hasHeightForWidth())
        self.export_2.setSizePolicy(sizePolicy)
        self.export_2.setObjectName("export_2")
        self.gridLayout.addWidget(self.export_2, 1, 0, 1, 1)
        self.open = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy)
        self.open.setObjectName("open")
        self.gridLayout.addWidget(self.open, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 4, 17), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.daily_confirmed = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_confirmed.sizePolicy().hasHeightForWidth())
        self.daily_confirmed.setSizePolicy(sizePolicy)
        self.daily_confirmed.setObjectName("daily_confirmed")
        self.gridLayout.addWidget(self.daily_confirmed, 4, 0, 1, 1)
        self.cum_confirmed = QtGui.QPushButton(self.centralwidget)
        self.cum_confirmed.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cum_confirmed.sizePolicy().hasHeightForWidth())
        self.cum_confirmed.setSizePolicy(sizePolicy)
        self.cum_confirmed.setObjectName("cum_confirmed")
        self.gridLayout.addWidget(self.cum_confirmed, 4, 1, 1, 1)
        self.daily_probable = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_probable.sizePolicy().hasHeightForWidth())
        self.daily_probable.setSizePolicy(sizePolicy)
        self.daily_probable.setObjectName("daily_probable")
        self.gridLayout.addWidget(self.daily_probable, 5, 0, 1, 1)
        self.cum_probable = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cum_probable.sizePolicy().hasHeightForWidth())
        self.cum_probable.setSizePolicy(sizePolicy)
        self.cum_probable.setObjectName("cum_probable")
        self.gridLayout.addWidget(self.cum_probable, 5, 1, 1, 1)
        self.daily_total = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_total.sizePolicy().hasHeightForWidth())
        self.daily_total.setSizePolicy(sizePolicy)
        self.daily_total.setObjectName("daily_total")
        self.gridLayout.addWidget(self.daily_total, 6, 0, 1, 1)
        self.cum_total = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cum_total.sizePolicy().hasHeightForWidth())
        self.cum_total.setSizePolicy(sizePolicy)
        self.cum_total.setObjectName("cum_total")
        self.gridLayout.addWidget(self.cum_total, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuNZ_COVID_19_Data_Processing = QtGui.QMenu(self.menubar)
        self.menuNZ_COVID_19_Data_Processing.setObjectName("menuNZ_COVID_19_Data_Processing")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuNZ_COVID_19_Data_Processing.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "COVID-19 NZ DATA", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:10pt; font-weight:600; color:#24292e; background-color:#ffffff;\">COVID-19 NZ Data Processing<br /></span><span style=\" font-size:8pt;\"><br /></span><span style=\" font-size:10pt;\">Plot and export daily data from COVID-19 cases in New Zealand from the Ministry of Health\'s website (</span><a href=\"https://health.govt.nz/\"><span style=\" font-family:\'-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji\'; font-size:10pt; text-decoration: underline; color:#0366d6; background-color:#ffffff;\">https://health.govt.nz</span></a><span style=\" font-size:10pt;\">).</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This app is part of a bigger project at the Auckland Bioengineering Institute</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(see </span><a href=\"https://github.com/ABI-Covid-19\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://github.com/ABI-Covid-19).</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.export_2.setText(QtGui.QApplication.translate("MainWindow", "Export all data", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.daily_confirmed.setText(QtGui.QApplication.translate("MainWindow", "Daily confirmed cases", None, QtGui.QApplication.UnicodeUTF8))
        self.cum_confirmed.setText(QtGui.QApplication.translate("MainWindow", "Cumulitative confirmed cases", None, QtGui.QApplication.UnicodeUTF8))
        self.daily_probable.setText(QtGui.QApplication.translate("MainWindow", "Daily probable cases", None, QtGui.QApplication.UnicodeUTF8))
        self.cum_probable.setText(QtGui.QApplication.translate("MainWindow", "Cumulitative probable cases", None, QtGui.QApplication.UnicodeUTF8))
        self.daily_total.setText(QtGui.QApplication.translate("MainWindow", "Daily total cases", None, QtGui.QApplication.UnicodeUTF8))
        self.cum_total.setText(QtGui.QApplication.translate("MainWindow", "Cumulitative total cases", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNZ_COVID_19_Data_Processing.setTitle(QtGui.QApplication.translate("MainWindow", "ABI-COVID-19", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

