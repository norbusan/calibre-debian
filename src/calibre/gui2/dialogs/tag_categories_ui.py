# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/tag_categories.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagCategories(object):
    def setupUi(self, TagCategories):
        TagCategories.setObjectName("TagCategories")
        TagCategories.resize(628, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("chapters.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TagCategories.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(TagCategories)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(TagCategories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.category_box = QtWidgets.QComboBox(TagCategories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(160)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_box.sizePolicy().hasHeightForWidth())
        self.category_box.setSizePolicy(sizePolicy)
        self.category_box.setMinimumSize(QtCore.QSize(145, 0))
        self.category_box.setEditable(False)
        self.category_box.setObjectName("category_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.category_box)
        self.label_5 = QtWidgets.QLabel(TagCategories)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.category_filter_box = QtWidgets.QComboBox(TagCategories)
        self.category_filter_box.setObjectName("category_filter_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.category_filter_box)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.delete_category_button = QtWidgets.QToolButton(TagCategories)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_category_button.setIcon(icon1)
        self.delete_category_button.setObjectName("delete_category_button")
        self.gridLayout.addWidget(self.delete_category_button, 0, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.input_box = QtWidgets.QLineEdit(TagCategories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy)
        self.input_box.setObjectName("input_box")
        self.hboxlayout.addWidget(self.input_box)
        self.add_category_button = QtWidgets.QToolButton(TagCategories)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_category_button.setIcon(icon2)
        self.add_category_button.setObjectName("add_category_button")
        self.hboxlayout.addWidget(self.add_category_button)
        self.gridLayout.addLayout(self.hboxlayout, 0, 1, 1, 1)
        self.rename_category_button = QtWidgets.QToolButton(TagCategories)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(I("edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_category_button.setIcon(icon3)
        self.rename_category_button.setObjectName("rename_category_button")
        self.gridLayout.addWidget(self.rename_category_button, 0, 2, 1, 1)
        self.apply_vl_checkbox = QtWidgets.QCheckBox(TagCategories)
        self.apply_vl_checkbox.setObjectName("apply_vl_checkbox")
        self.gridLayout.addWidget(self.apply_vl_checkbox, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 3)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label = QtWidgets.QLabel(TagCategories)
        self.label.setObjectName("label")
        self.hboxlayout1.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.available_items_box = QtWidgets.QListWidget(TagCategories)
        self.available_items_box.setAlternatingRowColors(True)
        self.available_items_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.available_items_box.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.available_items_box.setObjectName("available_items_box")
        self.hboxlayout2.addWidget(self.available_items_box)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.gridLayout_2.addLayout(self.vboxlayout, 1, 0, 1, 1)
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.apply_button = QtWidgets.QToolButton(TagCategories)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(I("forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon4)
        self.apply_button.setObjectName("apply_button")
        self.vboxlayout1.addWidget(self.apply_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.vboxlayout1, 1, 1, 1, 1)
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.label_2 = QtWidgets.QLabel(TagCategories)
        self.label_2.setObjectName("label_2")
        self.hboxlayout3.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem3)
        self.vboxlayout2.addLayout(self.hboxlayout3)
        self.applied_items_box = QtWidgets.QListWidget(TagCategories)
        self.applied_items_box.setAlternatingRowColors(True)
        self.applied_items_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.applied_items_box.setObjectName("applied_items_box")
        self.vboxlayout2.addWidget(self.applied_items_box)
        self.gridLayout_2.addLayout(self.vboxlayout2, 1, 2, 1, 1)
        self.vboxlayout3 = QtWidgets.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem4)
        self.unapply_button = QtWidgets.QToolButton(TagCategories)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(I("minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unapply_button.setIcon(icon5)
        self.unapply_button.setObjectName("unapply_button")
        self.vboxlayout3.addWidget(self.unapply_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.vboxlayout3, 1, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TagCategories)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 4)
        self.label_3.setBuddy(self.category_box)
        self.label_5.setBuddy(self.category_filter_box)
        self.label.setBuddy(self.available_items_box)
        self.label_2.setBuddy(self.applied_items_box)

        self.retranslateUi(TagCategories)
        self.buttonBox.accepted.connect(TagCategories.accept)
        self.buttonBox.rejected.connect(TagCategories.reject)
        QtCore.QMetaObject.connectSlotsByName(TagCategories)

    def retranslateUi(self, TagCategories):

        TagCategories.setWindowTitle(_("User categories editor"))
        self.label_3.setText(_("Category &name: "))
        self.category_box.setToolTip(_("Select a category to edit"))
        self.label_5.setText(_("&Category filter: "))
        self.category_filter_box.setToolTip(_("Select the content kind of the new category"))
        self.delete_category_button.setToolTip(_("Delete this selected tag category"))
        self.delete_category_button.setText(_("..."))
        self.input_box.setToolTip(_("Enter a category name, then use the add button or the rename button"))
        self.add_category_button.setToolTip(_("Add a new category"))
        self.add_category_button.setText(_("..."))
        self.rename_category_button.setToolTip(_("Rename the current category to what is in the box"))
        self.rename_category_button.setText(_("..."))
        self.apply_vl_checkbox.setToolTip(_("<p>Show items in the Available items box only if they appear in the\n"
"      current virtual library. Applied items not in the VL will be marked\n"
"      \"not on any book\".</p>"))
        self.apply_vl_checkbox.setText(_("&Show only available items in current virtual library"))
        self.label.setText(_("&Available items"))
        self.apply_button.setToolTip(_("Apply tags to current tag category"))
        self.apply_button.setText(_("..."))
        self.label_2.setText(_("Applied &items"))
        self.unapply_button.setToolTip(_("Unapply (remove) tag from current tag category"))
        self.unapply_button.setText(_("..."))

