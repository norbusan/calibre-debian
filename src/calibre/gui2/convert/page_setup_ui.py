# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/page_setup.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 476)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.opt_output_profile = QtWidgets.QListView(Form)
        self.opt_output_profile.setObjectName("opt_output_profile")
        self.verticalLayout_2.addWidget(self.opt_output_profile)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.profile_description = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_description.sizePolicy().hasHeightForWidth())
        self.profile_description.setSizePolicy(sizePolicy)
        self.profile_description.setText("")
        self.profile_description.setWordWrap(True)
        self.profile_description.setObjectName("profile_description")
        self.verticalLayout.addWidget(self.profile_description)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.opt_input_profile = QtWidgets.QListView(Form)
        self.opt_input_profile.setObjectName("opt_input_profile")
        self.verticalLayout_3.addWidget(self.opt_input_profile)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.opt_margin_left = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.opt_margin_left.setDecimals(1)
        self.opt_margin_left.setMinimum(-1.0)
        self.opt_margin_left.setMaximum(200.0)
        self.opt_margin_left.setObjectName("opt_margin_left")
        self.gridLayout.addWidget(self.opt_margin_left, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.opt_margin_top = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.opt_margin_top.setDecimals(1)
        self.opt_margin_top.setMinimum(-1.0)
        self.opt_margin_top.setMaximum(200.0)
        self.opt_margin_top.setObjectName("opt_margin_top")
        self.gridLayout.addWidget(self.opt_margin_top, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.opt_margin_right = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.opt_margin_right.setDecimals(1)
        self.opt_margin_right.setMinimum(-1.0)
        self.opt_margin_right.setMaximum(200.0)
        self.opt_margin_right.setObjectName("opt_margin_right")
        self.gridLayout.addWidget(self.opt_margin_right, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.opt_margin_bottom = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.opt_margin_bottom.setDecimals(1)
        self.opt_margin_bottom.setMinimum(-1.0)
        self.opt_margin_bottom.setMaximum(200.0)
        self.opt_margin_bottom.setObjectName("opt_margin_bottom")
        self.gridLayout.addWidget(self.opt_margin_bottom, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.opt_output_profile)
        self.label_2.setBuddy(self.opt_input_profile)
        self.label_3.setBuddy(self.opt_margin_left)
        self.label_4.setBuddy(self.opt_margin_top)
        self.label_5.setBuddy(self.opt_margin_right)
        self.label_6.setBuddy(self.opt_margin_bottom)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label.setText(_("&Output profile:"))
        self.groupBox.setTitle(_("Profile description"))
        self.label_2.setText(_("&Input profile:"))
        self.groupBox_2.setTitle(_("Margins"))
        self.label_3.setText(_("&Left:"))
        self.opt_margin_left.setSpecialValueText(_("Unchanged"))
        self.opt_margin_left.setSuffix(_(" pt"))
        self.label_4.setText(_("&Top:"))
        self.opt_margin_top.setSpecialValueText(_("Unchanged"))
        self.opt_margin_top.setSuffix(_(" pt"))
        self.label_5.setText(_("&Right:"))
        self.opt_margin_right.setSpecialValueText(_("Unchanged"))
        self.opt_margin_right.setSuffix(_(" pt"))
        self.label_6.setText(_("&Bottom:"))
        self.opt_margin_bottom.setSpecialValueText(_("Unchanged"))
        self.opt_margin_bottom.setSuffix(_(" pt"))

