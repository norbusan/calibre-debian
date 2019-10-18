# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/font_key.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 554)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("wizard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 3)
        self.wh_label = QtWidgets.QLabel(Dialog)
        self.wh_label.setWordWrap(True)
        self.wh_label.setOpenExternalLinks(True)
        self.wh_label.setObjectName("wh_label")
        self.gridLayout.addWidget(self.wh_label, 0, 0, 1, 4)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.font_size_key = QtWidgets.QLineEdit(self.groupBox_2)
        self.font_size_key.setObjectName("font_size_key")
        self.gridLayout_2.addWidget(self.font_size_key, 1, 2, 1, 1)
        self.output_base_font_size = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.output_base_font_size.setDecimals(1)
        self.output_base_font_size.setObjectName("output_base_font_size")
        self.gridLayout_2.addWidget(self.output_base_font_size, 0, 2, 1, 1)
        self.button_use_default = QtWidgets.QPushButton(self.groupBox_2)
        self.button_use_default.setObjectName("button_use_default")
        self.gridLayout_2.addWidget(self.button_use_default, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.input_base_font_size = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.input_base_font_size.setDecimals(1)
        self.input_base_font_size.setObjectName("input_base_font_size")
        self.gridLayout_3.addWidget(self.input_base_font_size, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.input_font_size = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_font_size.sizePolicy().hasHeightForWidth())
        self.input_font_size.setSizePolicy(sizePolicy)
        self.input_font_size.setMaximumSize(QtCore.QSize(130, 16777215))
        self.input_font_size.setDecimals(1)
        self.input_font_size.setObjectName("input_font_size")
        self.horizontalLayout.addWidget(self.input_font_size)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.input_mapped_font_size = QtWidgets.QLabel(self.groupBox)
        self.input_mapped_font_size.setObjectName("input_mapped_font_size")
        self.horizontalLayout.addWidget(self.input_mapped_font_size)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)
        self.label_3.setBuddy(self.output_base_font_size)
        self.label_4.setBuddy(self.font_size_key)
        self.label_5.setBuddy(self.input_base_font_size)
        self.label_6.setBuddy(self.input_font_size)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Font rescaling wizard"))
        self.wh_label.setText(_("<p>This wizard will help you choose an appropriate font size key for your needs. Just enter the base font size of the input document and then enter an input font size. The wizard will display what font size it will be mapped to, by the font rescaling algorithm. You can adjust the algorithm by adjusting the output base font size and font key below. When you find values suitable for you, click OK.</p>\n"
"<p>By default, if the output base font size is zero and/or no font size key is specified, calibre will use the values from the current Output profile. </p>\n"
"<p>See the <a href=\"%s\">User Manual</a> for an explanation of how font size rescaling works.</p>"))
        self.groupBox_2.setTitle(_("&Output document"))
        self.label_3.setText(_("&Base font size:"))
        self.label_4.setText(_("Font size &key:"))
        self.output_base_font_size.setSuffix(_(" pt"))
        self.button_use_default.setText(_("Use &default values"))
        self.groupBox.setTitle(_("&Input document"))
        self.label_5.setText(_("&Base font size:"))
        self.input_base_font_size.setSuffix(_(" pt"))
        self.label_6.setText(_("&Font size: "))
        self.input_font_size.setSuffix(_(" pt"))
        self.label_7.setText(_(" will map to size: "))
        self.input_mapped_font_size.setText(_("0.0 pt"))

