# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daisy_creator_mag.ui'
#
# Created: Fri May  6 12:11:54 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DaisyMain(object):
    def setupUi(self, DaisyMain):
        DaisyMain.setObjectName(_fromUtf8("DaisyMain"))
        DaisyMain.resize(809, 781)
        self.centralwidget = QtGui.QWidget(DaisyMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButtonClose1 = QtGui.QPushButton(self.tab)
        self.pushButtonClose1.setGeometry(QtCore.QRect(650, 630, 111, 27))
        self.pushButtonClose1.setObjectName(_fromUtf8("pushButtonClose1"))
        self.checkBoxCopyChangeNr1000 = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyChangeNr1000.setGeometry(QtCore.QRect(29, 478, 301, 22))
        self.checkBoxCopyChangeNr1000.setObjectName(_fromUtf8("checkBoxCopyChangeNr1000"))
        self.lineEditCopyFile1 = QtGui.QLineEdit(self.tab)
        self.lineEditCopyFile1.setGeometry(QtCore.QRect(24, 182, 610, 27))
        self.lineEditCopyFile1.setObjectName(_fromUtf8("lineEditCopyFile1"))
        self.toolButtonCopyDest = QtGui.QToolButton(self.tab)
        self.toolButtonCopyDest.setGeometry(QtCore.QRect(640, 127, 24, 25))
        self.toolButtonCopyDest.setObjectName(_fromUtf8("toolButtonCopyDest"))
        self.label_1 = QtGui.QLabel(self.tab)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.checkBoxCopyBhzIntro = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBhzIntro.setGeometry(QtCore.QRect(336, 418, 301, 22))
        self.checkBoxCopyBhzIntro.setObjectName(_fromUtf8("checkBoxCopyBhzIntro"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 268, 610, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.toolButtonCopySource = QtGui.QToolButton(self.tab)
        self.toolButtonCopySource.setGeometry(QtCore.QRect(640, 94, 24, 25))
        self.toolButtonCopySource.setObjectName(_fromUtf8("toolButtonCopySource"))
        self.toolButtonCopyFile2 = QtGui.QToolButton(self.tab)
        self.toolButtonCopyFile2.setGeometry(QtCore.QRect(640, 216, 24, 25))
        self.toolButtonCopyFile2.setObjectName(_fromUtf8("toolButtonCopyFile2"))
        self.toolButtonCopyFile1 = QtGui.QToolButton(self.tab)
        self.toolButtonCopyFile1.setGeometry(QtCore.QRect(640, 183, 24, 25))
        self.toolButtonCopyFile1.setObjectName(_fromUtf8("toolButtonCopyFile1"))
        self.checkBoxCopyBitrateChange = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBitrateChange.setGeometry(QtCore.QRect(29, 448, 301, 22))
        self.checkBoxCopyBitrateChange.setObjectName(_fromUtf8("checkBoxCopyBitrateChange"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 159, 610, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEditCopyDest = QtGui.QLineEdit(self.tab)
        self.lineEditCopyDest.setGeometry(QtCore.QRect(24, 126, 610, 27))
        self.lineEditCopyDest.setObjectName(_fromUtf8("lineEditCopyDest"))
        self.checkBoxCopyID3Change = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyID3Change.setEnabled(True)
        self.checkBoxCopyID3Change.setGeometry(QtCore.QRect(336, 448, 301, 22))
        self.checkBoxCopyID3Change.setObjectName(_fromUtf8("checkBoxCopyID3Change"))
        self.comboBoxCopyBhz = QtGui.QComboBox(self.tab)
        self.comboBoxCopyBhz.setGeometry(QtCore.QRect(24, 290, 610, 27))
        self.comboBoxCopyBhz.setObjectName(_fromUtf8("comboBoxCopyBhz"))
        self.lineEditCopyFile2 = QtGui.QLineEdit(self.tab)
        self.lineEditCopyFile2.setGeometry(QtCore.QRect(24, 215, 610, 27))
        self.lineEditCopyFile2.setObjectName(_fromUtf8("lineEditCopyFile2"))
        self.checkBoxCopyBhzAusgAnsage = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyBhzAusgAnsage.setGeometry(QtCore.QRect(29, 418, 301, 22))
        self.checkBoxCopyBhzAusgAnsage.setObjectName(_fromUtf8("checkBoxCopyBhzAusgAnsage"))
        self.lineEditCopySource = QtGui.QLineEdit(self.tab)
        self.lineEditCopySource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditCopySource.setObjectName(_fromUtf8("lineEditCopySource"))
        self.checkBoxCopyChangeNr1001 = QtGui.QCheckBox(self.tab)
        self.checkBoxCopyChangeNr1001.setGeometry(QtCore.QRect(336, 478, 301, 22))
        self.checkBoxCopyChangeNr1001.setObjectName(_fromUtf8("checkBoxCopyChangeNr1001"))
        self.comboBoxCopyBhzAusg = QtGui.QComboBox(self.tab)
        self.comboBoxCopyBhzAusg.setGeometry(QtCore.QRect(24, 320, 610, 27))
        self.comboBoxCopyBhzAusg.setObjectName(_fromUtf8("comboBoxCopyBhzAusg"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.checkBoxDaisyIgnoreTitleDigits = QtGui.QCheckBox(self.tab)
        self.checkBoxDaisyIgnoreTitleDigits.setGeometry(QtCore.QRect(29, 510, 291, 22))
        self.checkBoxDaisyIgnoreTitleDigits.setObjectName(_fromUtf8("checkBoxDaisyIgnoreTitleDigits"))
        self.comboBoxPrefBitrate = QtGui.QComboBox(self.tab)
        self.comboBoxPrefBitrate.setGeometry(QtCore.QRect(30, 630, 610, 27))
        self.comboBoxPrefBitrate.setObjectName(_fromUtf8("comboBoxPrefBitrate"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(30, 610, 71, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.checkBoxDaisyLevel = QtGui.QCheckBox(self.tab)
        self.checkBoxDaisyLevel.setGeometry(QtCore.QRect(336, 510, 271, 22))
        self.checkBoxDaisyLevel.setObjectName(_fromUtf8("checkBoxDaisyLevel"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 560, 281, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBoxDaisyTrenner = QtGui.QComboBox(self.tab)
        self.comboBoxDaisyTrenner.setGeometry(QtCore.QRect(30, 580, 610, 27))
        self.comboBoxDaisyTrenner.setObjectName(_fromUtf8("comboBoxDaisyTrenner"))
        self.checkBoxDaisyDateCalendar = QtGui.QCheckBox(self.tab)
        self.checkBoxDaisyDateCalendar.setGeometry(QtCore.QRect(336, 540, 391, 22))
        self.checkBoxDaisyDateCalendar.setObjectName(_fromUtf8("checkBoxDaisyDateCalendar"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 390, 610, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.tab_4)
        self.commandLinkButton.setGeometry(QtCore.QRect(650, 450, 111, 161))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.textEdit = QtGui.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(24, 90, 610, 521))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.progressBarCopy = QtGui.QProgressBar(self.tab_4)
        self.progressBarCopy.setGeometry(QtCore.QRect(24, 630, 610, 25))
        self.progressBarCopy.setProperty("value", 24)
        self.progressBarCopy.setObjectName(_fromUtf8("progressBarCopy"))
        self.pushButtonClose1_2 = QtGui.QPushButton(self.tab_4)
        self.pushButtonClose1_2.setGeometry(QtCore.QRect(650, 630, 111, 27))
        self.pushButtonClose1_2.setObjectName(_fromUtf8("pushButtonClose1_2"))
        self.line_4 = QtGui.QFrame(self.tab_4)
        self.line_4.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_3 = QtGui.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(0, 60, 790, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEditMetaSource = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaSource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditMetaSource.setObjectName(_fromUtf8("lineEditMetaSource"))
        self.toolButtonMetaFile = QtGui.QToolButton(self.tab_3)
        self.toolButtonMetaFile.setGeometry(QtCore.QRect(640, 93, 24, 25))
        self.toolButtonMetaFile.setObjectName(_fromUtf8("toolButtonMetaFile"))
        self.lineEditMetaProducer = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaProducer.setGeometry(QtCore.QRect(160, 150, 471, 27))
        self.lineEditMetaProducer.setObjectName(_fromUtf8("lineEditMetaProducer"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 155, 121, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.commandLinkButtonMeta = QtGui.QCommandLinkButton(self.tab_3)
        self.commandLinkButtonMeta.setGeometry(QtCore.QRect(640, 150, 131, 261))
        self.commandLinkButtonMeta.setObjectName(_fromUtf8("commandLinkButtonMeta"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(30, 180, 121, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEditMetaAutor = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaAutor.setGeometry(QtCore.QRect(160, 180, 471, 27))
        self.lineEditMetaAutor.setObjectName(_fromUtf8("lineEditMetaAutor"))
        self.lineEditMetaTitle = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaTitle.setGeometry(QtCore.QRect(160, 210, 471, 27))
        self.lineEditMetaTitle.setObjectName(_fromUtf8("lineEditMetaTitle"))
        self.lineEditMetaEdition = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaEdition.setGeometry(QtCore.QRect(160, 240, 471, 27))
        self.lineEditMetaEdition.setObjectName(_fromUtf8("lineEditMetaEdition"))
        self.lineEditMetaNarrator = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaNarrator.setGeometry(QtCore.QRect(160, 270, 471, 27))
        self.lineEditMetaNarrator.setObjectName(_fromUtf8("lineEditMetaNarrator"))
        self.lineEditMetaKeywords = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaKeywords.setGeometry(QtCore.QRect(160, 300, 471, 27))
        self.lineEditMetaKeywords.setObjectName(_fromUtf8("lineEditMetaKeywords"))
        self.lineEditMetaRefOrig = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaRefOrig.setGeometry(QtCore.QRect(160, 330, 471, 27))
        self.lineEditMetaRefOrig.setObjectName(_fromUtf8("lineEditMetaRefOrig"))
        self.lineEditMetaPublisher = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaPublisher.setGeometry(QtCore.QRect(160, 360, 471, 27))
        self.lineEditMetaPublisher.setObjectName(_fromUtf8("lineEditMetaPublisher"))
        self.lineEditMetaYear = QtGui.QLineEdit(self.tab_3)
        self.lineEditMetaYear.setGeometry(QtCore.QRect(160, 390, 471, 27))
        self.lineEditMetaYear.setObjectName(_fromUtf8("lineEditMetaYear"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(30, 210, 121, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(30, 240, 121, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 270, 121, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(30, 300, 121, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(30, 330, 121, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(30, 360, 121, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(30, 390, 121, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 610, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 833, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 610, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.toolButtonDaisySource = QtGui.QToolButton(self.tab_2)
        self.toolButtonDaisySource.setGeometry(QtCore.QRect(640, 93, 24, 25))
        self.toolButtonDaisySource.setObjectName(_fromUtf8("toolButtonDaisySource"))
        self.lineEditDaisySource = QtGui.QLineEdit(self.tab_2)
        self.lineEditDaisySource.setGeometry(QtCore.QRect(24, 93, 610, 27))
        self.lineEditDaisySource.setObjectName(_fromUtf8("lineEditDaisySource"))
        self.textEditDaisy = QtGui.QTextEdit(self.tab_2)
        self.textEditDaisy.setGeometry(QtCore.QRect(24, 140, 610, 471))
        self.textEditDaisy.setObjectName(_fromUtf8("textEditDaisy"))
        self.commandLinkButtonDaisy = QtGui.QCommandLinkButton(self.tab_2)
        self.commandLinkButtonDaisy.setGeometry(QtCore.QRect(650, 420, 111, 191))
        self.commandLinkButtonDaisy.setObjectName(_fromUtf8("commandLinkButtonDaisy"))
        self.progressBarDaisy = QtGui.QProgressBar(self.tab_2)
        self.progressBarDaisy.setGeometry(QtCore.QRect(24, 630, 610, 25))
        self.progressBarDaisy.setProperty("value", 24)
        self.progressBarDaisy.setObjectName(_fromUtf8("progressBarDaisy"))
        self.pushButtonClose2 = QtGui.QPushButton(self.tab_2)
        self.pushButtonClose2.setGeometry(QtCore.QRect(650, 630, 111, 27))
        self.pushButtonClose2.setObjectName(_fromUtf8("pushButtonClose2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.textEditHelp = QtGui.QTextEdit(self.tab_5)
        self.textEditHelp.setGeometry(QtCore.QRect(0, 0, 791, 691))
        self.textEditHelp.setObjectName(_fromUtf8("textEditHelp"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.textEditUserHelp = QtGui.QTextEdit(self.tab_6)
        self.textEditUserHelp.setGeometry(QtCore.QRect(0, 0, 791, 691))
        self.textEditUserHelp.setObjectName(_fromUtf8("textEditUserHelp"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        DaisyMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DaisyMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DaisyMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DaisyMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DaisyMain.setStatusBar(self.statusbar)

        self.retranslateUi(DaisyMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DaisyMain)

    def retranslateUi(self, DaisyMain):
        DaisyMain.setWindowTitle(_translate("DaisyMain", "Daisy-Creator", None))
        self.pushButtonClose1.setText(_translate("DaisyMain", "Quit", None))
        self.checkBoxCopyChangeNr1000.setText(_translate("DaisyMain", "1000 in 0100 umbenennen", None))
        self.lineEditCopyFile1.setText(_translate("DaisyMain", "Datei 1 waehlen", None))
        self.toolButtonCopyDest.setToolTip(_translate("DaisyMain", "Zielverzeichnis", None))
        self.toolButtonCopyDest.setText(_translate("DaisyMain", "...", None))
        self.label_1.setText(_translate("DaisyMain", "Daisy - Settings", None))
        self.checkBoxCopyBhzIntro.setText(_translate("DaisyMain", "Intro kopieren", None))
        self.label_4.setText(_translate("DaisyMain", "Bhz und Ausgabe", None))
        self.toolButtonCopySource.setToolTip(_translate("DaisyMain", "Quellverzeichnis", None))
        self.toolButtonCopySource.setText(_translate("DaisyMain", "...", None))
        self.toolButtonCopyFile2.setText(_translate("DaisyMain", "...", None))
        self.toolButtonCopyFile1.setText(_translate("DaisyMain", "...", None))
        self.checkBoxCopyBitrateChange.setText(_translate("DaisyMain", "Bitrate anpassen", None))
        self.label_6.setText(_translate("DaisyMain", "Zusatz-Dateien", None))
        self.lineEditCopyDest.setText(_translate("DaisyMain", "Ziel-Ordner", None))
        self.checkBoxCopyID3Change.setText(_translate("DaisyMain", "ID3-Tags entfernen", None))
        self.lineEditCopyFile2.setText(_translate("DaisyMain", "Datei 2 waehlen", None))
        self.checkBoxCopyBhzAusgAnsage.setText(_translate("DaisyMain", "Ausgabe-Ansage kopieren", None))
        self.lineEditCopySource.setText(_translate("DaisyMain", "Quell-Ordner", None))
        self.checkBoxCopyChangeNr1001.setText(_translate("DaisyMain", "1001 in 0100 umbenennen", None))
        self.label_2.setText(_translate("DaisyMain", "Quelle und Ziel", None))
        self.checkBoxDaisyIgnoreTitleDigits.setToolTip(_translate("DaisyMain", "Fuehrende Ziffern aus Dateinamen fuer Titel ignorieren (vor dem Kopieren einstellen!)", None))
        self.checkBoxDaisyIgnoreTitleDigits.setText(_translate("DaisyMain", "Führende Ziffern fuer Titel entfernen", None))
        self.label_13.setText(_translate("DaisyMain", "Datenrate", None))
        self.checkBoxDaisyLevel.setText(_translate("DaisyMain", "Ebenen aus Dateinamen ermitteln", None))
        self.label_7.setText(_translate("DaisyMain", "Trenner für Autor und Titel", None))
        self.checkBoxDaisyDateCalendar.setText(_translate("DaisyMain", "Datum aus Dateinamen ermitteln (z.B. fuer Kalender)", None))
        self.label_14.setText(_translate("DaisyMain", "Einstellungen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DaisyMain", "1 Settings", None))
        self.commandLinkButton.setText(_translate("DaisyMain", "Kopieren", None))
        self.pushButtonClose1_2.setText(_translate("DaisyMain", "Quit", None))
        self.label_12.setText(_translate("DaisyMain", "Copy - Tool", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("DaisyMain", "2 Copy", None))
        self.label_8.setText(_translate("DaisyMain", "Daisy - Metadaten", None))
        self.label_9.setText(_translate("DaisyMain", "Quelldatei der Metadaten", None))
        self.lineEditMetaSource.setText(_translate("DaisyMain", "Metadaten-Datei waehlen", None))
        self.toolButtonMetaFile.setText(_translate("DaisyMain", "...", None))
        self.lineEditMetaProducer.setText(_translate("DaisyMain", "Produzent", None))
        self.label_10.setText(_translate("DaisyMain", "Produzent", None))
        self.commandLinkButtonMeta.setText(_translate("DaisyMain", "Meta laden", None))
        self.label_11.setText(_translate("DaisyMain", "Autor", None))
        self.lineEditMetaAutor.setText(_translate("DaisyMain", "Autor", None))
        self.lineEditMetaTitle.setText(_translate("DaisyMain", "Titel", None))
        self.lineEditMetaEdition.setText(_translate("DaisyMain", "Edition", None))
        self.lineEditMetaNarrator.setText(_translate("DaisyMain", "Sprecher", None))
        self.lineEditMetaKeywords.setText(_translate("DaisyMain", "Stichworte", None))
        self.lineEditMetaRefOrig.setText(_translate("DaisyMain", "Ref-Original", None))
        self.lineEditMetaPublisher.setText(_translate("DaisyMain", "Verlag", None))
        self.lineEditMetaYear.setText(_translate("DaisyMain", "Erscheinungsjahr", None))
        self.label_15.setText(_translate("DaisyMain", "Titel", None))
        self.label_16.setText(_translate("DaisyMain", "Edition", None))
        self.label_17.setText(_translate("DaisyMain", "Sprecher", None))
        self.label_18.setText(_translate("DaisyMain", "Stichworte", None))
        self.label_19.setText(_translate("DaisyMain", "Ref-Original", None))
        self.label_20.setText(_translate("DaisyMain", "Verlag", None))
        self.label_21.setText(_translate("DaisyMain", "Erscheinungsjahr", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DaisyMain", "2 Meta", None))
        self.label_3.setText(_translate("DaisyMain", "Daisy - Tool", None))
        self.label_5.setText(_translate("DaisyMain", "Quelle", None))
        self.toolButtonDaisySource.setToolTip(_translate("DaisyMain", "Quellverzeichnis", None))
        self.toolButtonDaisySource.setText(_translate("DaisyMain", "...", None))
        self.lineEditDaisySource.setText(_translate("DaisyMain", "Quell-Ordner", None))
        self.commandLinkButtonDaisy.setText(_translate("DaisyMain", "Daisyfizieren", None))
        self.pushButtonClose2.setText(_translate("DaisyMain", "Quit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DaisyMain", "3 Daisy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("DaisyMain", "Help", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("DaisyMain", "User Help", None))

