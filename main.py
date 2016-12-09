from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import platform
from PyQt4.QtCore import QTime,QTimer
from PyQt4.QtCore import *
from threading import Timer
from subprocess import check_call

import os ,ctypes , subprocess , time , datetime , sys
from time import strftime
from PowerManager import Ui_Form

def Restart():
    os.system(r'Shutdown.exe -r -t 00')
def ShutDown():
    os.system(r'Shutdown.exe -s -t 00')
def Sleep():
    os.system(r'Rundll32.exe powrprof.dll,SetSuspendState Standby')

def LockScreen():## دالة قفل الشاشة
    #ctypes.windll.user32.LockWorkStation()  # lockscreen
    os.system(r'Rundll32.exe user32.dll,LockWorkStation')

def Hebernate(): # دالة إغلاق الطاقة
    if sys.platform == "linux" or sys.platform == "linux2":
        # linux
        print("linux")
    elif sys.platform == "darwin":
        # MAC OS X
        print("mac")

    elif sys.platform == "win32":
        os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
        # Windows
def LogOff():
    os.system(r'')



class main (QWidget , Ui_Form):
    def __init__(self): # constractor
        QWidget.__init__(self)
        self.setupUi(self)
        self.timer = QTimer(self)
        self.start_time = 00
        self.timer.timeout.connect(self.updateLCD)
        self.LcdTime()## إظهار الوقت الحالي

    def After(self, enabled):  # تفعيل اختيار الدقائق
        if enabled:
            self.min.setEnabled(True)
        else:
            self.Time_After.display()
    def submit(self):  #التطبيق عند الضغط على زر تنفيذ
        if self.heber.isChecked():#عند تفعيل زر إغلاق الطاقة
            if self.now.isChecked():### عند تفعيل خيار الآن
                Hebernate()##استدعاء دالةاغلاق الطاقة
            elif self.after.isChecked():
                self.countdown()#### اظهار العد التنازلي لتنفيذ المهمة
                self.Minute(Hebernate)#استدعاء دالة الدقائق#
        if self.lock.isChecked():###عند اختيار قفل الشاشة###
            if self.after.isChecked():
                self.countdown()
                self.Minute(LockScreen)
            elif self.now.isChecked():
                LockScreen()
        if self.sleep.isChecked():
            if self.after.isChecked():
                self.countdown()
                self.Minute(Sleep)
            elif self.now.isChecked:
                Sleep()
        if self.restart.isChecked:
            if self.after.isChecked:
                self.countdown()
                self.Minute(Restart)
            elif self.now.isChecked:
                Restart()
        if self.logoff.isChecked:
            if self.after.isChecked:
                self.countdown()
                self.Minute(LogOff)
            elif self.now.isChecked:
                LogOff()

    def Minute(self,function):
        t = self.min.value() * 60
        v = Timer(t, function)
        v.start()


###############إظهار وف المهمة لكل اختيار###############
    def info(self):
        if self.heber.isChecked():###إغلاق الشاشة###
            self.info.setText("إيقاف تشغيل الجهاز كليا مع الإبقاء على البرامج والملفات التي تم العمل عليها مفتوحة عند تشغيل الجهاز من جديد")
        elif self.lock.isChecked():###قفل الشاشة###
            self.info.setText("قفل الشاشة ")
            # now = datetime.datetime.now()
            # self.time_label.setText(str(datetime.datetime.now()))
        elif self.shutdown.isChecked():###إيقاف التشغيل###
            self.info.setText("إيقاف تشغيل الجهاز كليا")
        elif self.restart.isChecked():#إعادة التشغيل#
            self.info.setText("إعادة تشغيل الجهاز(قبل التنفيذ قم بحفظ كافة أعمالك) ")
        elif self.logoff.isChecked():#تسجيل الخروج#
            self.info.setText("إغلاق جلسة المستخدم ")
        elif self.sleep.isChecked():#وضع الاسبات#
            self.info.setText("وضع الإسبات ")
##########################

############إظهار التوقيت الحالي###########

    def LcdTime(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        # Reduced update time to fasten the change from w/ secs to w/o secs
        timer.start(1)

    def Time(self):
        time = QTime.currentTime().toString()
        self.CurTime.display(time)

###############العد التنازلي###############
    def countdown(self):

        # Reset the timer and the lcd
        self.timer.stop()
        self.start_time = self.min.value() * 60
        #self.Time_After.display("%d:%02d" % (self.start_time / 60, self.start_time % 60))
        self.label_4.setText("%d:%02d" % (self.start_time / 60, self.start_time % 60))
        # Restart the timer
        self.timer.start(1000)
    def updateLCD(self):###تحديث التوقيت التنازلي####
        # Update the lcd
        self.start_time -= 1
        if self.start_time >= 0:
            #self.Time_After.display("%02d:%02d" % (self.start_time / 60,self.start_time % 60 ))
            self.label_4.setText("%d:%02d" % (self.start_time / 60, self.start_time % 60))
        else:
            self.timer.stop()

    



app=QApplication(sys.argv)
window = main()
window.show()
app.exec()