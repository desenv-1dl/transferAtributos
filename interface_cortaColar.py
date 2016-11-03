# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_cortaColar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(348, 380)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
       
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
	self.pushButton_4.clicked.connect(self.teste)
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
	self.addItems()
	self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def addItems(self):
	b = ['1', '2', '3', '4', '5']
	self.listWidget.addItems(b)
	for i in range(self.listWidget.count()):
		self.listWidget.item(i).setCheckState(QtCore.Qt.Checked)

    def teste(self):	
	for i in range(self.listWidget.count()):
		if self.listWidget.item(i).checkState():
			print self.listWidget.item(i).text()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Transferir atributos", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("Dialog", "Colar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

