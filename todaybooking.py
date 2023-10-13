# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todaybooking.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
from showdetails import *
from pescribe import *

class Ui_todaybooking(object):
    
    def setupUi(self, todaybooking):
        todaybooking.setObjectName("todaybooking")
        todaybooking.resize(991, 600)
        self.centralwidget = QtWidgets.QWidget(todaybooking)
        self.centralwidget.setObjectName("centralwidget")
        self.todaybooking_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.todaybooking_2.setGeometry(QtCore.QRect(150, 60, 681, 241))
        self.todaybooking_2.setObjectName("todaybooking_2")
        self.todaybooking_2.setColumnCount(5)
        self.todaybooking_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.todaybooking_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.todaybooking_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.todaybooking_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.todaybooking_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.todaybooking_2.setHorizontalHeaderItem(4, item)
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(190, 410, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")

        self.b1.clicked.connect(self.showdetails)

        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(622, 410, 151, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")

        self.b2.clicked.connect(self.pescribe)

        todaybooking.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(todaybooking)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 26))
        self.menubar.setObjectName("menubar")
        todaybooking.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(todaybooking)
        self.statusbar.setObjectName("statusbar")
        todaybooking.setStatusBar(self.statusbar)

        self.retranslateUi(todaybooking)
        QtCore.QMetaObject.connectSlotsByName(todaybooking)
        self.display()

    def retranslateUi(self, todaybooking):
        _translate = QtCore.QCoreApplication.translate
        todaybooking.setWindowTitle(_translate("todaybooking", "MainWindow"))
        item = self.todaybooking_2.horizontalHeaderItem(0)
        item.setText(_translate("todaybooking", "PID"))
        item = self.todaybooking_2.horizontalHeaderItem(1)
        item.setText(_translate("todaybooking", "NAME"))
        item = self.todaybooking_2.horizontalHeaderItem(2)
        item.setText(_translate("todaybooking", "PHONE"))
        item = self.todaybooking_2.horizontalHeaderItem(3)
        item.setText(_translate("todaybooking", "DOCTOR"))
        item = self.todaybooking_2.horizontalHeaderItem(4)
        item.setText(_translate("todaybooking", "SYMPTOMS"))
        self.b1.setText(_translate("todaybooking", "showpatientdetails"))
        self.b2.setText(_translate("todaybooking", "prescribe"))

    def display(self):
        import sqlite3
        conn = sqlite3.connect("dms.db")
        cur = conn.cursor()
        date=datetime.now()
        d=date.strftime("%d-%m-%Y")
        
        v=(d,)

        sql="select * from booking where date=?"
        cur.execute(sql,v)
        data=cur.fetchall()
        for i in data:
            pid=i[0]
            sqlp="select * from patient where pid=?"
            cur.execute(sqlp,(pid,))
            datap=cur.fetchall()
            n=datap[0][1]
            p=datap[0][2]
            doctor=i[1]
            symptom=i[2]
            date=i[3]
            rowPosition = self.todaybooking_2.rowCount()
            self.todaybooking_2.insertRow(rowPosition)
            self.todaybooking_2.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(pid)))
            self.todaybooking_2.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(n))
            self.todaybooking_2.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(p))
            self.todaybooking_2.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(doctor))
            self.todaybooking_2.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(symptom))
            self.todaybooking_2.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(date))
        conn.close()

    def showdetails(self):
        selected_row = self.todaybooking_2.currentRow()
        pid = self.todaybooking_2.item(selected_row, 0).text()
        self.showdetails = QtWidgets.QMainWindow()
        self.ui = Ui_showdetails(pid)
        self.ui.setupUi(self.showdetails)
        self.showdetails.show()


    def pescribe(self):
        selected_row = self.todaybooking_2.currentRow()
        pid = self.todaybooking_2.item(selected_row, 0).text()
        self.pescribe = QtWidgets.QMainWindow()
        self.ui = Ui_pescribe(pid)
        self.ui.setupUi(self.pescribe)
        self.pescribe.show()

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    todaybooking = QtWidgets.QMainWindow()
    ui = Ui_todaybooking()
    ui.setupUi(todaybooking)
    todaybooking.show()
    sys.exit(app.exec_())
