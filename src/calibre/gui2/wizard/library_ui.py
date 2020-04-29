# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/wizard/library.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(614, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(WizardPage)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.language = QtWidgets.QComboBox(WizardPage)
        self.language.setObjectName("language")
        self.horizontalLayout.addWidget(self.language)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.libloc_label1 = QtWidgets.QLabel(WizardPage)
        self.libloc_label1.setWordWrap(True)
        self.libloc_label1.setObjectName("libloc_label1")
        self.verticalLayout.addWidget(self.libloc_label1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.location = QtWidgets.QLineEdit(WizardPage)
        self.location.setReadOnly(True)
        self.location.setObjectName("location")
        self.horizontalLayout_2.addWidget(self.location)
        self.button_change = QtWidgets.QPushButton(WizardPage)
        self.button_change.setObjectName("button_change")
        self.horizontalLayout_2.addWidget(self.button_change)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.libloc_label2 = QtWidgets.QLabel(WizardPage)
        self.libloc_label2.setWordWrap(True)
        self.libloc_label2.setObjectName("libloc_label2")
        self.verticalLayout.addWidget(self.libloc_label2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.move_lib_label = QtWidgets.QLabel(WizardPage)
        self.move_lib_label.setText("")
        self.move_lib_label.setTextFormat(QtCore.Qt.RichText)
        self.move_lib_label.setWordWrap(True)
        self.move_lib_label.setOpenExternalLinks(True)
        self.move_lib_label.setObjectName("move_lib_label")
        self.verticalLayout.addWidget(self.move_lib_label)
        self.label_3.setBuddy(self.language)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):

        WizardPage.setWindowTitle(_("WizardPage"))
        WizardPage.setTitle(_("Welcome to calibre"))
        WizardPage.setSubTitle(_("The one stop solution to all your e-book needs."))
        self.label_3.setText(_("Choose your &language:"))
        self.libloc_label1.setText(_("<p>Choose a location for your books. When you add books to calibre, they will be copied here. Use an <b>empty folder</b> for a new calibre library:"))
        self.button_change.setText(_("&Change"))
        self.libloc_label2.setText(_("If a calibre library already exists at the newly selected location, calibre will use it automatically."))
