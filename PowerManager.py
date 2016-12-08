# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'power-manger.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import platform
from PyQt4.QtCore import QTime,QTimer
from PyQt4.QtCore import *
from threading import Thread


import os ,ctypes , subprocess , time , datetime , sys
from time import strftime

#os.system('C:\\Users\silent\\Desktop\ssifat-assalat-othman-khamiss.mp4')
#subprocess.call(["shutdown", "/l"]) # log off
#os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')#hibernate
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


class Ui_Form(object):



    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(599, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("D:/Untitled-3.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-color: #2b303b;"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 581, 61))
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setStyleSheet(_fromUtf8("color: rgb(255, 234, 0);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.restart = QtGui.QRadioButton(self.groupBox)
        self.restart.toggled.connect(self.info)  ##############################
        self.restart.setGeometry(QtCore.QRect(120, 21, 89, 17))
        self.restart.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.restart.setObjectName(_fromUtf8("restart"))
        self.sleep = QtGui.QRadioButton(self.groupBox)
        self.sleep.toggled.connect(self.info)  ########################
        self.sleep.setGeometry(QtCore.QRect(303, 21, 83, 17))
        self.sleep.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.sleep.setObjectName(_fromUtf8("sleep"))
        self.logoff = QtGui.QRadioButton(self.groupBox)
        self.logoff.toggled.connect(self.info)  ##################
        self.logoff.setGeometry(QtCore.QRect(489, 21, 90, 17))
        self.logoff.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.logoff.setObjectName(_fromUtf8("logoff"))
        self.lock = QtGui.QRadioButton(self.groupBox)
        self.lock.toggled.connect(self.info)  #############
        self.lock.setGeometry(QtCore.QRect(31, 21, 83, 17))
        self.lock.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lock.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.lock.setObjectName(_fromUtf8("lock"))
        self.heber = QtGui.QRadioButton(self.groupBox)
        self.heber.toggled.connect(self.info)  ###########################
        self.heber.setGeometry(QtCore.QRect(215, 21, 82, 17))
        self.heber.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.heber.setObjectName(_fromUtf8("heber"))
        self.shutdown = QtGui.QRadioButton(self.groupBox)
        self.shutdown.toggled.connect(self.info)  ########################
        self.shutdown.setGeometry(QtCore.QRect(392, 21, 91, 17))
        self.shutdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.shutdown.setObjectName(_fromUtf8("shutdown"))
        self.heber.raise_()
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 160, 261, 61))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setStyleSheet(_fromUtf8("color: rgb(255, 234, 0);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.now = QtGui.QRadioButton(self.groupBox_2)
        self.now.setGeometry(QtCore.QRect(160, 20, 82, 17))
        self.now.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.now.setObjectName(_fromUtf8("now"))
        self.after = QtGui.QRadioButton(self.groupBox_2)
        self.after.toggled.connect(self.After)  ###################
        self.after.setGeometry(QtCore.QRect(90, 20, 82, 17))
        self.after.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.after.setObjectName(_fromUtf8("after"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.min = QtGui.QSpinBox(self.groupBox_2)
        self.min.setMaximum(1000)
        self.min.setSuffix(" min")
        self.min.valueChanged.connect(self.After)
        self.min.setEnabled(False)
        self.min.setGeometry(QtCore.QRect(70, 20, 62, 22))
        self.min.setWhatsThis(_fromUtf8(""))
        self.min.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.min.setObjectName(_fromUtf8("min"))
        self.done = QtGui.QPushButton(Form)
        self.done.clicked.connect(self.submit)
       # self.done.clicked.connect(self.handleButton)

        self.done.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.done.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.done.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.done.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);\n"
                                          "alternate-background-color: rgb(107, 104, 101);\n"
                                          "gridline-color: rgb(255, 255, 255);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-color: rgb(255, 255, 255);"))
        self.done.setCheckable(False)
        self.done.setAutoDefault(False)
        self.done.setDefault(False)
        self.done.setFlat(False)
        self.done.setObjectName(_fromUtf8("done"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 71, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 100, 581, 61))
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setStyleSheet(_fromUtf8("color: rgb(255, 234, 0);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.info = QtGui.QLabel(self.groupBox_3)
        self.info.setGeometry(QtCore.QRect(10, 19, 561, 31))
        self.info.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.info.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.info.setObjectName(_fromUtf8("info"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 170, 121, 16))
        self.label_3.setStyleSheet(_fromUtf8("color:#63a832;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.CurTime = QtGui.QLCDNumber(Form)
        self.CurTime.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.CurTime.setAcceptDrops(False)
        self.CurTime.setStyleSheet(_fromUtf8("background-color: rgb(240, 243, 255);\n"
                                             "font: 75 8pt \"MS Shell Dlg 2\";"))
        self.CurTime.setFrameShape(QtGui.QFrame.Panel)
        self.CurTime.setFrameShadow(QtGui.QFrame.Sunken)
        self.CurTime.setSmallDecimalPoint(True)
        self.CurTime.setNumDigits(8)
        self.CurTime.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.CurTime.setProperty("intValue", 0)
        self.CurTime.setObjectName(_fromUtf8("CurTime_2"))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 190, 71, 20))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Form)





    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "برنامج التحكم في الطاقة", None))
        self.groupBox.setTitle(_translate("Form", "اختر المهمة", None))
        self.restart.setText(_translate("Form", "إعادة التشغيل", None))
        self.sleep.setText(_translate("Form", "وضع الإسبات", None))
        self.logoff.setText(_translate("Form", "تسجيل الخروج", None))
        self.lock.setText(_translate("Form", "قفل الشاشة", None))
        self.heber.setText(_translate("Form", "إغلاق الطاقة", None))
        self.shutdown.setText(_translate("Form", "إيقاف التشغيل", None))
        self.groupBox_2.setTitle(_translate("Form", "الوقت", None))
        self.now.setText(_translate("Form", "الآن", None))
        self.after.setText(_translate("Form", "بعد", None))
        self.label.setText(_translate("Form", "دقيقة", None))
        self.done.setText(_translate("Form", "تنفيذ", None))
        self.label_2.setText(_translate("Form", "الوقت الحالي:", None))
        self.groupBox_3.setTitle(_translate("Form", "وصف المهمة", None))
        self.info.setText(_translate("Form", "فضلا حدد المهمة التي تود القيام بها", None))
        self.label_3.setText(_translate("Form", "سيتم تنفيذ المهمة بعد:", None))





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

