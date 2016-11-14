# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/comic_input.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 398)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.opt_colors = QtWidgets.QSpinBox(Form)
        self.opt_colors.setMinimum(8)
        self.opt_colors.setMaximum(32000000)
        self.opt_colors.setSingleStep(8)
        self.opt_colors.setObjectName("opt_colors")
        self.gridLayout.addWidget(self.opt_colors, 3, 1, 1, 1)
        self.opt_dont_normalize = QtWidgets.QCheckBox(Form)
        self.opt_dont_normalize.setObjectName("opt_dont_normalize")
        self.gridLayout.addWidget(self.opt_dont_normalize, 5, 0, 1, 1)
        self.opt_keep_aspect_ratio = QtWidgets.QCheckBox(Form)
        self.opt_keep_aspect_ratio.setObjectName("opt_keep_aspect_ratio")
        self.gridLayout.addWidget(self.opt_keep_aspect_ratio, 6, 0, 1, 1)
        self.opt_dont_sharpen = QtWidgets.QCheckBox(Form)
        self.opt_dont_sharpen.setObjectName("opt_dont_sharpen")
        self.gridLayout.addWidget(self.opt_dont_sharpen, 7, 0, 1, 1)
        self.opt_disable_trim = QtWidgets.QCheckBox(Form)
        self.opt_disable_trim.setObjectName("opt_disable_trim")
        self.gridLayout.addWidget(self.opt_disable_trim, 8, 0, 1, 1)
        self.opt_wide = QtWidgets.QCheckBox(Form)
        self.opt_wide.setObjectName("opt_wide")
        self.gridLayout.addWidget(self.opt_wide, 9, 0, 1, 1)
        self.opt_landscape = QtWidgets.QCheckBox(Form)
        self.opt_landscape.setObjectName("opt_landscape")
        self.gridLayout.addWidget(self.opt_landscape, 10, 0, 1, 1)
        self.opt_right2left = QtWidgets.QCheckBox(Form)
        self.opt_right2left.setObjectName("opt_right2left")
        self.gridLayout.addWidget(self.opt_right2left, 11, 0, 1, 1)
        self.opt_no_sort = QtWidgets.QCheckBox(Form)
        self.opt_no_sort.setObjectName("opt_no_sort")
        self.gridLayout.addWidget(self.opt_no_sort, 12, 0, 1, 1)
        self.opt_despeckle = QtWidgets.QCheckBox(Form)
        self.opt_despeckle.setObjectName("opt_despeckle")
        self.gridLayout.addWidget(self.opt_despeckle, 13, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.opt_no_process = QtWidgets.QCheckBox(Form)
        self.opt_no_process.setObjectName("opt_no_process")
        self.gridLayout.addWidget(self.opt_no_process, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 14, 0, 1, 1)
        self.opt_output_format = QtWidgets.QComboBox(Form)
        self.opt_output_format.setObjectName("opt_output_format")
        self.gridLayout.addWidget(self.opt_output_format, 14, 1, 1, 1)
        self.opt_dont_grayscale = QtWidgets.QCheckBox(Form)
        self.opt_dont_grayscale.setObjectName("opt_dont_grayscale")
        self.gridLayout.addWidget(self.opt_dont_grayscale, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.opt_comic_image_size = QtWidgets.QLineEdit(Form)
        self.opt_comic_image_size.setObjectName("opt_comic_image_size")
        self.gridLayout.addWidget(self.opt_comic_image_size, 4, 1, 1, 1)
        self.opt_dont_add_comic_pages_to_toc = QtWidgets.QCheckBox(Form)
        self.opt_dont_add_comic_pages_to_toc.setObjectName("opt_dont_add_comic_pages_to_toc")
        self.gridLayout.addWidget(self.opt_dont_add_comic_pages_to_toc, 2, 0, 1, 2)
        self.label_3.setBuddy(self.opt_colors)
        self.label.setBuddy(self.opt_output_format)
        self.label_2.setBuddy(self.opt_comic_image_size)

        self.retranslateUi(Form)
        self.opt_no_process.toggled['bool'].connect(self.label_3.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_colors.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_dont_normalize.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_keep_aspect_ratio.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_dont_sharpen.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_disable_trim.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_wide.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_landscape.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_right2left.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_no_sort.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_despeckle.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_output_format.setDisabled)
        self.opt_no_process.toggled['bool'].connect(self.opt_dont_grayscale.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label_3.setText(_("&Number of Colors:"))
        self.opt_dont_normalize.setText(_("Disable &normalize"))
        self.opt_keep_aspect_ratio.setText(_("Keep &aspect ratio"))
        self.opt_dont_sharpen.setText(_("Disable &Sharpening"))
        self.opt_disable_trim.setText(_("Disable &Trimming"))
        self.opt_wide.setText(_("&Wide"))
        self.opt_landscape.setText(_("&Landscape"))
        self.opt_right2left.setText(_("&Right to left"))
        self.opt_no_sort.setText(_("Don\'t so&rt"))
        self.opt_despeckle.setText(_("De&speckle"))
        self.opt_no_process.setText(_("&Disable comic processing"))
        self.label.setText(_("&Output format:"))
        self.opt_dont_grayscale.setText(_("Disable conversion of images to &black and white"))
        self.label_2.setText(_("Override image &size:"))
        self.opt_dont_add_comic_pages_to_toc.setText(_("Don\'t add links to &pages to the Table of Contents for CBC files"))

