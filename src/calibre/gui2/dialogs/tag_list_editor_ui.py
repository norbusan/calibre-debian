# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/c3/src/calibre/gui2/dialogs/tag_list_editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagListEditor(object):
    def setupUi(self, TagListEditor):
        TagListEditor.setObjectName("TagListEditor")
        TagListEditor.resize(397, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("chapters.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TagListEditor.setWindowIcon(icon)
        self.gridlayout = QtWidgets.QGridLayout(TagListEditor)
        self.gridlayout.setObjectName("gridlayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(TagListEditor)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.search_box = HistoryLineEdit(TagListEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_11.addWidget(self.search_box)
        self.search_button = QtWidgets.QPushButton(TagListEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_11.addWidget(self.search_button)
        self.gridlayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 2)
        self.apply_vl_checkbox = QtWidgets.QCheckBox(TagListEditor)
        self.apply_vl_checkbox.setObjectName("apply_vl_checkbox")
        self.gridlayout.addWidget(self.apply_vl_checkbox, 1, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.delete_button = QtWidgets.QToolButton(TagListEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon2)
        self.delete_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_2.addWidget(self.delete_button)
        self.rename_button = QtWidgets.QToolButton(TagListEditor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("edit_input.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_button.setIcon(icon3)
        self.rename_button.setIconSize(QtCore.QSize(32, 32))
        self.rename_button.setObjectName("rename_button")
        self.verticalLayout_2.addWidget(self.rename_button)
        self.undo_button = QtWidgets.QToolButton(TagListEditor)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(I("edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_button.setIcon(icon4)
        self.undo_button.setIconSize(QtCore.QSize(32, 32))
        self.undo_button.setObjectName("undo_button")
        self.verticalLayout_2.addWidget(self.undo_button)
        self.gridlayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(TagListEditor)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridlayout.addWidget(self.table, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TagListEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.label.setBuddy(self.search_box)

        self.retranslateUi(TagListEditor)
        self.buttonBox.accepted.connect(TagListEditor.accept)
        self.buttonBox.rejected.connect(TagListEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(TagListEditor)

    def retranslateUi(self, TagListEditor):

        TagListEditor.setWindowTitle(_("Category editor"))
        self.label.setText(_("&Search for:"))
        self.search_box.setToolTip(_("Search for an item in the Tag column"))
        self.search_button.setToolTip(_("Display items containing the search string"))
        self.search_button.setText(_("&Find"))
        self.apply_vl_checkbox.setToolTip(_("<p>Show items in the Available items box only if they appear in the\n"
"      current virtual library. Applied items not in the VL will be marked\n"
"      \"not on any book\".</p>"))
        self.apply_vl_checkbox.setText(_("&Show only available items in current virtual library"))
        self.delete_button.setToolTip(_("Delete item from database. This will unapply the item from all books and then remove it from the database."))
        self.delete_button.setText(_("..."))
        self.delete_button.setShortcut(_("Ctrl+D"))
        self.rename_button.setToolTip(_("Rename the item in every book where it is used."))
        self.rename_button.setText(_("..."))
        self.rename_button.setShortcut(_("Ctrl+R"))
        self.undo_button.setToolTip(_("Undo any deletes or edits on the selected lines"))
        self.undo_button.setText(_("..."))
        self.undo_button.setShortcut(_("Ctrl+U"))
from calibre.gui2.widgets import HistoryLineEdit

