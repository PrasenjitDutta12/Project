# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addattendence.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_addattendence(object):
    def setupUi(self, addattendence):
        addattendence.setObjectName("addattendence")
        addattendence.resize(848, 600)
        self.centralwidget = QtWidgets.QWidget(addattendence)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(20, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(20, 150, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(20, 210, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(20, 260, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(300, 20, 511, 41))
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(300, 80, 511, 41))
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(300, 140, 511, 41))
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(300, 210, 511, 41))
        self.line4.setObjectName("line4")
        self.line5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line5.setGeometry(QtCore.QRect(300, 270, 511, 41))
        self.line5.setObjectName("line5")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(290, 390, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")

        self.b1.clicked.connect(self.add)

        addattendence.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addattendence)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        addattendence.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addattendence)
        self.statusbar.setObjectName("statusbar")
        addattendence.setStatusBar(self.statusbar)

        self.retranslateUi(addattendence)
        QtCore.QMetaObject.connectSlotsByName(addattendence)

    def retranslateUi(self, addattendence):
        _translate = QtCore.QCoreApplication.translate
        addattendence.setWindowTitle(_translate("addattendence", "MainWindow"))
        self.l1.setText(_translate("addattendence", "Name"))
        self.l2.setText(_translate("addattendence", "Phone No"))
        self.l3.setText(_translate("addattendence", "Email ID"))
        self.l4.setText(_translate("addattendence", "Enter Password"))
        self.l5.setText(_translate("addattendence", "Re Enter Password"))
        self.b1.setText(_translate("addattendence", "ADD"))

    def add(self):
        import sqlite3
        conn=sqlite3.connect("dms.db")
        cur=conn.cursor()
        a=self.line1.text()
        b=self.line2.text()
        c=self.line3.text()
        d=self.line4.text()
        e=self.line5.text()
        if(a==""):
            print("1")
        elif(b==""):
            print("2")
        elif(b.isdigit()==False):
             print("3")
        elif len(b)!=10:
            print("4")
        elif(c==""):
            print("5")
        elif(d==""):
            print("6")
        elif len(d)<8 or len(d)>15: 
            print("7")
        elif(e==""):
            print("8")
        elif len(e)<8 or len(e)>15:
            print("10")
        elif(d!=e):
            print("9")

        else:
            sql = "select count(*) from attendent where Eid = ? or phno = ?"
            v1 = (c, b)  
            cur.execute(sql, v1)
            conn.commit()
            result = cur.fetchall()
            rc = result[0][0] 
            if rc > 0: 
                print("Email ID or Phone number already exists")
            else:
                sql = "insert into attendent values(?,?,?,?)"
                v2 = (a, b, c, d,)
                cur.execute(sql, v2)  
                conn.commit() 
                rc = cur.rowcount 
                
                print("Admin registered successfully")
        conn.close()
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addattendence = QtWidgets.QMainWindow()
    ui = Ui_addattendence()
    ui.setupUi(addattendence)
    addattendence.show()
    sys.exit(app.exec_())
