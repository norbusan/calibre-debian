# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/edit_authors_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditAuthorsDialog(object):
    def setupUi(self, EditAuthorsDialog):
        EditAuthorsDialog.setObjectName("EditAuthorsDialog")
        EditAuthorsDialog.resize(768, 342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditAuthorsDialog.sizePolicy().hasHeightForWidth())
        EditAuthorsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditAuthorsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(EditAuthorsDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.find_box = HistoryLineEdit(EditAuthorsDialog)
        self.find_box.setMinimumSize(QtCore.QSize(200, 0))
        self.find_box.setClearButtonEnabled(True)
        self.find_box.setObjectName("find_box")
        self.gridlayout.addWidget(self.find_box, 0, 1, 1, 1)
        self.find_button = QtWidgets.QPushButton(EditAuthorsDialog)
        self.find_button.setObjectName("find_button")
        self.gridlayout.addWidget(self.find_button, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 3, 1, 1)
        self.apply_vl_checkbox = QtWidgets.QCheckBox(EditAuthorsDialog)
        self.apply_vl_checkbox.setObjectName("apply_vl_checkbox")
        self.gridlayout.addWidget(self.apply_vl_checkbox, 0, 4, 1, 1)
        self.label1 = QtWidgets.QLabel(EditAuthorsDialog)
        self.label1.setObjectName("label1")
        self.gridlayout.addWidget(self.label1, 1, 0, 1, 1)
        self.filter_box = HistoryLineEdit(EditAuthorsDialog)
        self.filter_box.setMinimumSize(QtCore.QSize(200, 0))
        self.filter_box.setClearButtonEnabled(True)
        self.filter_box.setObjectName("filter_box")
        self.gridlayout.addWidget(self.filter_box, 1, 1, 1, 1)
        self.filter_button = QtWidgets.QPushButton(EditAuthorsDialog)
        self.filter_button.setObjectName("filter_button")
        self.gridlayout.addWidget(self.filter_button, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.table = QtWidgets.QTableWidget(EditAuthorsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setColumnCount(0)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.gridlayout1 = QtWidgets.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        self.recalc_author_sort = QtWidgets.QPushButton(EditAuthorsDialog)
        self.recalc_author_sort.setObjectName("recalc_author_sort")
        self.gridlayout1.addWidget(self.recalc_author_sort, 1, 0, 1, 1)
        self.auth_sort_to_author = QtWidgets.QPushButton(EditAuthorsDialog)
        self.auth_sort_to_author.setObjectName("auth_sort_to_author")
        self.gridlayout1.addWidget(self.auth_sort_to_author, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditAuthorsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout1.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout1)
        self.label.setBuddy(self.find_box)
        self.label1.setBuddy(self.filter_box)

        self.retranslateUi(EditAuthorsDialog)
        self.buttonBox.accepted.connect(EditAuthorsDialog.accept)
        self.buttonBox.rejected.connect(EditAuthorsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditAuthorsDialog)

    def retranslateUi(self, EditAuthorsDialog):

        EditAuthorsDialog.setWindowTitle(_("Manage authors"))
        self.label.setText(_("&Search for:"))
        self.find_button.setText(_("S&earch"))
        self.apply_vl_checkbox.setToolTip(_("<p>Only show authors in the\n"
"          current Virtual library. Edits already done may be hidden but will\n"
"          not be forgotten.</p>"))
        self.apply_vl_checkbox.setText(_("Only show authors in the current &virtual library"))
        self.label1.setText(_("Filter &By:"))
        self.filter_box.setToolTip(_("<p>Only show authors that contain the text in this box.\n"
"          The match ignores case.</p>"))
        self.filter_button.setText(_("Fi&lter"))
        self.recalc_author_sort.setToolTip(_("Reset all the author sort values to a value automatically\n"
"generated from the author. Exactly how this value is automatically\n"
"generated can be controlled via Preferences->Advanced->Tweaks"))
        self.recalc_author_sort.setText(_("&Recalculate all author sort values"))
        self.auth_sort_to_author.setToolTip(_("Copy author sort to author for every author. You typically use this button\n"
"after changing Preferences->Advanced->Tweaks->Author sort name algorithm"))
        self.auth_sort_to_author.setText(_("&Copy all author sort values to author"))
from calibre.gui2.widgets import HistoryLineEdit
