# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/search_and_replace.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(667, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sr_search = RegexEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_search.sizePolicy().hasHeightForWidth())
        self.sr_search.setSizePolicy(sizePolicy)
        self.sr_search.setObjectName("sr_search")
        self.gridLayout_2.addWidget(self.sr_search, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.sr_replace = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_replace.sizePolicy().hasHeightForWidth())
        self.sr_replace.setSizePolicy(sizePolicy)
        self.sr_replace.setObjectName("sr_replace")
        self.gridLayout_2.addWidget(self.sr_replace, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, -1, -1, -1)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.sr_add = QtWidgets.QPushButton(Form)
        self.sr_add.setObjectName("sr_add")
        self.buttonsLayout.addWidget(self.sr_add)
        self.sr_change = QtWidgets.QPushButton(Form)
        self.sr_change.setEnabled(False)
        self.sr_change.setObjectName("sr_change")
        self.buttonsLayout.addWidget(self.sr_change)
        self.sr_remove = QtWidgets.QPushButton(Form)
        self.sr_remove.setEnabled(False)
        self.sr_remove.setObjectName("sr_remove")
        self.buttonsLayout.addWidget(self.sr_remove)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.buttonsLayout.addWidget(self.frame)
        self.sr_load = QtWidgets.QPushButton(Form)
        self.sr_load.setObjectName("sr_load")
        self.buttonsLayout.addWidget(self.sr_load)
        self.sr_save = QtWidgets.QPushButton(Form)
        self.sr_save.setEnabled(False)
        self.sr_save.setObjectName("sr_save")
        self.buttonsLayout.addWidget(self.sr_save)
        self.gridLayout_4.addLayout(self.buttonsLayout, 2, 0, 1, 1)
        self.searchReplaceLayout = QtWidgets.QHBoxLayout()
        self.searchReplaceLayout.setContentsMargins(0, -1, -1, -1)
        self.searchReplaceLayout.setObjectName("searchReplaceLayout")
        self.search_replace = QtWidgets.QTableWidget(Form)
        self.search_replace.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.search_replace.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.search_replace.setObjectName("search_replace")
        self.search_replace.setColumnCount(0)
        self.search_replace.setRowCount(0)
        self.searchReplaceLayout.addWidget(self.search_replace)
        self.positionLayout = QtWidgets.QVBoxLayout()
        self.positionLayout.setObjectName("positionLayout")
        self.sr_up = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_up.sizePolicy().hasHeightForWidth())
        self.sr_up.setSizePolicy(sizePolicy)
        self.sr_up.setMaximumSize(QtCore.QSize(32, 16777215))
        self.sr_up.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("arrow-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sr_up.setIcon(icon)
        self.sr_up.setObjectName("sr_up")
        self.positionLayout.addWidget(self.sr_up)
        self.sr_down = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_down.sizePolicy().hasHeightForWidth())
        self.sr_down.setSizePolicy(sizePolicy)
        self.sr_down.setMaximumSize(QtCore.QSize(32, 16777215))
        self.sr_down.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("arrow-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sr_down.setIcon(icon1)
        self.sr_down.setObjectName("sr_down")
        self.positionLayout.addWidget(self.sr_down)
        self.searchReplaceLayout.addLayout(self.positionLayout)
        self.gridLayout_4.addLayout(self.searchReplaceLayout, 3, 0, 1, 1)
        self.rh_label = QtWidgets.QLabel(Form)
        self.rh_label.setWordWrap(True)
        self.rh_label.setOpenExternalLinks(True)
        self.rh_label.setObjectName("rh_label")
        self.gridLayout_4.addWidget(self.rh_label, 0, 0, 1, 1)
        self.label_4.setBuddy(self.sr_replace)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Edit search/replace definition"))
        self.label_4.setText(_("&Replacement text:"))
        self.sr_add.setToolTip(_("Add the current expression to the list of expressions that will be applied"))
        self.sr_add.setText(_("&Add"))
        self.sr_change.setToolTip(_("Edit the currently selected expression"))
        self.sr_change.setText(_("&Change"))
        self.sr_remove.setToolTip(_("Remove the currently selected expression"))
        self.sr_remove.setText(_("&Remove"))
        self.sr_load.setToolTip(_("Load a list of expressions from a previously saved file"))
        self.sr_load.setText(_("&Load"))
        self.sr_save.setToolTip(_("Save this list of expressions so that you can re-use it easily"))
        self.sr_save.setText(_("&Save"))
        self.sr_up.setToolTip(_("Move expression up."))
        self.sr_down.setToolTip(_("Move expression down."))
        self.rh_label.setText(_("<p>Search and replace uses <i>regular expressions</i>. See the <a href=\"%s\">regular expressions tutorial</a> to get started with regular expressions. Also clicking the wizard button below will allow you to test your regular expression against the current input document. When you are happy with an expression, click the Add button to add it to the list of expressions."))
from calibre.gui2.convert.regex_builder import RegexEdit

