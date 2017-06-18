# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/template_functions.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 672)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.function_name = QtWidgets.QComboBox(Form)
        self.function_name.setEditable(True)
        self.function_name.setObjectName("function_name")
        self.gridLayout_3.addWidget(self.function_name, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.argument_count = QtWidgets.QSpinBox(Form)
        self.argument_count.setMinimum(-1)
        self.argument_count.setObjectName("argument_count")
        self.gridLayout_3.addWidget(self.argument_count, 1, 1, 1, 1)
        self.documentation = QtWidgets.QTextEdit(Form)
        self.documentation.setObjectName("documentation")
        self.gridLayout_3.addWidget(self.documentation, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_button = QtWidgets.QPushButton(Form)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_2.addWidget(self.clear_button)
        self.delete_button = QtWidgets.QPushButton(Form)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.replace_button = QtWidgets.QPushButton(Form)
        self.replace_button.setObjectName("replace_button")
        self.horizontalLayout_2.addWidget(self.replace_button)
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_2.addWidget(self.create_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout1 = QtWidgets.QVBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.label_41 = QtWidgets.QLabel(Form)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout1.addWidget(self.label_41)
        self.program = QtWidgets.QPlainTextEdit(Form)
        self.program.setMinimumSize(QtCore.QSize(400, 0))
        self.program.setDocumentTitle("")
        self.program.setTabStopWidth(30)
        self.program.setObjectName("program")
        self.horizontalLayout1.addWidget(self.program)
        self.horizontalLayout.addLayout(self.horizontalLayout1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.label_2.setBuddy(self.function_name)
        self.label_3.setBuddy(self.argument_count)
        self.label_4.setBuddy(self.documentation)
        self.label_41.setBuddy(self.program)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label_2.setText(_("&Function:"))
        self.function_name.setToolTip(_("Enter the name of the function to create."))
        self.label_3.setText(_("Argument &count:"))
        self.argument_count.setToolTip(_("Set this to -1 if the function takes a variable number of arguments"))
        self.label_4.setText(_("&Documentation:"))
        self.clear_button.setText(_("&Clear"))
        self.delete_button.setText(_("&Delete"))
        self.replace_button.setText(_("&Replace"))
        self.create_button.setText(_("C&reate"))
        self.label_41.setText(_("&Program code (Follow Python indenting rules):"))

