# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/tag_editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagEditor(object):
    def setupUi(self, TagEditor):
        TagEditor.setObjectName("TagEditor")
        TagEditor.resize(640, 666)
        self.verticalLayout = QtWidgets.QVBoxLayout(TagEditor)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(TagEditor)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.add_tag_input = EnLineEdit(TagEditor)
        self.add_tag_input.setObjectName("add_tag_input")
        self.horizontalLayout_4.addWidget(self.add_tag_input)
        self.add_tag_button = QtWidgets.QToolButton(TagEditor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_tag_button.setIcon(icon)
        self.add_tag_button.setObjectName("add_tag_button")
        self.horizontalLayout_4.addWidget(self.add_tag_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(TagEditor)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.available_filter_input = QtWidgets.QLineEdit(TagEditor)
        self.available_filter_input.setClearButtonEnabled(True)
        self.available_filter_input.setObjectName("available_filter_input")
        self.gridLayout.addWidget(self.available_filter_input, 1, 0, 1, 1)
        self.available_tags = QtWidgets.QListWidget(TagEditor)
        self.available_tags.setAlternatingRowColors(True)
        self.available_tags.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.available_tags.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.available_tags.setObjectName("available_tags")
        self.gridLayout.addWidget(self.available_tags, 2, 0, 1, 2)
        self.delete_button = QtWidgets.QPushButton(TagEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(TagEditor)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.apply_button = QtWidgets.QToolButton(TagEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon2)
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout.addWidget(self.apply_button)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.applied_filter_input = QtWidgets.QLineEdit(TagEditor)
        self.applied_filter_input.setClearButtonEnabled(True)
        self.applied_filter_input.setObjectName("applied_filter_input")
        self.gridLayout_2.addWidget(self.applied_filter_input, 1, 0, 1, 1)
        self.applied_tags = QtWidgets.QListWidget(TagEditor)
        self.applied_tags.setAlternatingRowColors(True)
        self.applied_tags.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.applied_tags.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.applied_tags.setObjectName("applied_tags")
        self.gridLayout_2.addWidget(self.applied_tags, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(TagEditor)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.unapply_button = QtWidgets.QPushButton(TagEditor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unapply_button.setIcon(icon3)
        self.unapply_button.setObjectName("unapply_button")
        self.gridLayout_2.addWidget(self.unapply_button, 3, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(TagEditor)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.buttonBox = QtWidgets.QDialogButtonBox(TagEditor)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.add_tag_input)
        self.label.setBuddy(self.available_tags)
        self.label_2.setBuddy(self.applied_tags)

        self.retranslateUi(TagEditor)
        self.buttonBox.accepted.connect(TagEditor.accept)
        self.buttonBox.rejected.connect(TagEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(TagEditor)

    def retranslateUi(self, TagEditor):

        TagEditor.setWindowTitle(_("Tag editor"))
        self.label_3.setText(_("&Add tag:"))
        self.add_tag_input.setToolTip(_("If the tag you want is not in the available list, you can add it here. Accepts a comma separated list of tags."))
        self.add_tag_button.setToolTip(_("Add tag to available tags and apply it to current book"))
        self.add_tag_button.setText(_("..."))
        self.available_filter_input.setPlaceholderText(_("Filter the available tags"))
        self.delete_button.setToolTip(_("Delete tag from database. This will unapply the tag from all books and then remove it from the database."))
        self.delete_button.setText(_("&Delete tag"))
        self.label.setText(_("Ava&ilable tags"))
        self.apply_button.setToolTip(_("Apply tag to current book"))
        self.apply_button.setText(_("..."))
        self.applied_filter_input.setPlaceholderText(_("Filter the applied tags"))
        self.label_2.setText(_("Applied &tags"))
        self.unapply_button.setToolTip(_("Unapply (remove) tag from current book"))
        self.unapply_button.setText(_("&Unapply tag"))
from calibre.gui2.widgets import EnLineEdit

