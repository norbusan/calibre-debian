# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/template_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TemplateDialog(object):
    def setupUi(self, TemplateDialog):
        TemplateDialog.setObjectName("TemplateDialog")
        TemplateDialog.resize(588, 546)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TemplateDialog.sizePolicy().hasHeightForWidth())
        TemplateDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(TemplateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.color_layout = QtWidgets.QWidget(TemplateDialog)
        self.color_layout.setObjectName("color_layout")
        self.gridlayout = QtWidgets.QGridLayout(self.color_layout)
        self.gridlayout.setObjectName("gridlayout")
        self.colored_field_label = QtWidgets.QLabel(self.color_layout)
        self.colored_field_label.setObjectName("colored_field_label")
        self.gridlayout.addWidget(self.colored_field_label, 0, 0, 1, 1)
        self.colored_field = QtWidgets.QComboBox(self.color_layout)
        self.colored_field.setObjectName("colored_field")
        self.gridlayout.addWidget(self.colored_field, 0, 1, 1, 1)
        self.color_chooser_label = QtWidgets.QLabel(self.color_layout)
        self.color_chooser_label.setObjectName("color_chooser_label")
        self.gridlayout.addWidget(self.color_chooser_label, 1, 0, 1, 1)
        self.color_name = ColorButton(self.color_layout)
        self.color_name.setObjectName("color_name")
        self.gridlayout.addWidget(self.color_name, 1, 1, 1, 1)
        self.color_copy_button = QtWidgets.QToolButton(self.color_layout)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("edit-copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color_copy_button.setIcon(icon)
        self.color_copy_button.setObjectName("color_copy_button")
        self.gridlayout.addWidget(self.color_copy_button, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.color_layout)
        self.icon_layout = QtWidgets.QWidget(TemplateDialog)
        self.icon_layout.setObjectName("icon_layout")
        self.gridlayout1 = QtWidgets.QGridLayout(self.icon_layout)
        self.gridlayout1.setObjectName("gridlayout1")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.icon_kind_label = QtWidgets.QLabel(self.icon_layout)
        self.icon_kind_label.setObjectName("icon_kind_label")
        self.hboxlayout.addWidget(self.icon_kind_label)
        self.icon_kind = QtWidgets.QComboBox(self.icon_layout)
        self.icon_kind.setObjectName("icon_kind")
        self.hboxlayout.addWidget(self.icon_kind)
        self.gridlayout1.addLayout(self.hboxlayout, 0, 0, 1, 2)
        self.icon_chooser_label = QtWidgets.QLabel(self.icon_layout)
        self.icon_chooser_label.setObjectName("icon_chooser_label")
        self.gridlayout1.addWidget(self.icon_chooser_label, 1, 0, 1, 1)
        self.icon_field = QtWidgets.QComboBox(self.icon_layout)
        self.icon_field.setObjectName("icon_field")
        self.gridlayout1.addWidget(self.icon_field, 1, 1, 1, 1)
        self.image_chooser_label = QtWidgets.QLabel(self.icon_layout)
        self.image_chooser_label.setObjectName("image_chooser_label")
        self.gridlayout1.addWidget(self.image_chooser_label, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.icon_layout)
        self.widget.setObjectName("widget")
        self.hboxlayout1 = QtWidgets.QHBoxLayout(self.widget)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.icon_files = QtWidgets.QComboBox(self.widget)
        self.icon_files.setObjectName("icon_files")
        self.hboxlayout1.addWidget(self.icon_files)
        self.icon_copy_button = QtWidgets.QToolButton(self.widget)
        self.icon_copy_button.setIcon(icon)
        self.icon_copy_button.setObjectName("icon_copy_button")
        self.hboxlayout1.addWidget(self.icon_copy_button)
        self.filename_button = QtWidgets.QPushButton(self.widget)
        self.filename_button.setObjectName("filename_button")
        self.hboxlayout1.addWidget(self.filename_button)
        self.gridlayout1.addWidget(self.widget, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.icon_layout)
        self.textbox = QtWidgets.QPlainTextEdit(TemplateDialog)
        self.textbox.setObjectName("textbox")
        self.verticalLayout.addWidget(self.textbox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(TemplateDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.template_value = QtWidgets.QLineEdit(TemplateDialog)
        self.template_value.setReadOnly(True)
        self.template_value.setObjectName("template_value")
        self.gridLayout.addWidget(self.template_value, 5, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(TemplateDialog)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 6, 0, 1, 1)
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.font_size_box = QtWidgets.QSpinBox(TemplateDialog)
        self.font_size_box.setObjectName("font_size_box")
        self.gridLayout1.addWidget(self.font_size_box, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout1.addItem(spacerItem, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TemplateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout1.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 6, 1, 1, 1)
        self.frame = QtWidgets.QFrame(TemplateDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 7, 0, 1, 2)
        self.label2 = QtWidgets.QLabel(TemplateDialog)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 8, 0, 1, 1)
        self.function = QtWidgets.QComboBox(TemplateDialog)
        self.function.setObjectName("function")
        self.gridLayout.addWidget(self.function, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(TemplateDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(TemplateDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.documentation = QtWidgets.QPlainTextEdit(TemplateDialog)
        self.documentation.setMaximumSize(QtCore.QSize(16777215, 75))
        self.documentation.setObjectName("documentation")
        self.gridLayout.addWidget(self.documentation, 9, 1, 1, 1)
        self.source_code = QtWidgets.QPlainTextEdit(TemplateDialog)
        self.source_code.setObjectName("source_code")
        self.gridLayout.addWidget(self.source_code, 10, 1, 1, 1)
        self.template_tutorial = QtWidgets.QLabel(TemplateDialog)
        self.template_tutorial.setOpenExternalLinks(True)
        self.template_tutorial.setObjectName("template_tutorial")
        self.gridLayout.addWidget(self.template_tutorial, 11, 1, 1, 1)
        self.template_func_reference = QtWidgets.QLabel(TemplateDialog)
        self.template_func_reference.setOpenExternalLinks(True)
        self.template_func_reference.setObjectName("template_func_reference")
        self.gridLayout.addWidget(self.template_func_reference, 12, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.colored_field_label.setBuddy(self.colored_field)
        self.color_chooser_label.setBuddy(self.color_name)
        self.icon_chooser_label.setBuddy(self.icon_field)
        self.image_chooser_label.setBuddy(self.color_name)
        self.label.setBuddy(self.template_value)
        self.label2.setBuddy(self.function)
        self.label_2.setBuddy(self.documentation)
        self.label_3.setBuddy(self.source_code)

        self.retranslateUi(TemplateDialog)
        self.buttonBox.accepted.connect(TemplateDialog.accept)
        self.buttonBox.rejected.connect(TemplateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateDialog)

    def retranslateUi(self, TemplateDialog):

        TemplateDialog.setWindowTitle(_("Edit template"))
        self.colored_field_label.setText(_("Set the color of the column:"))
        self.color_chooser_label.setText(_("Copy a color name to the clipboard:"))
        self.color_copy_button.setToolTip(_("Copy the selected color name to the clipboard"))
        self.icon_kind_label.setText(_("Kind:"))
        self.icon_chooser_label.setText(_("Apply the icon to column:"))
        self.image_chooser_label.setText(_("Copy an icon file name to the clipboard:"))
        self.icon_copy_button.setToolTip(_("Copy the selected icon file name to the clipboard"))
        self.filename_button.setText(_("Add icon"))
        self.filename_button.setToolTip(_("Add an icon file to the set of choices"))
        self.label.setText(_("Template value:"))
        self.label.setToolTip(_("The value of the template using the current book in the library view"))
        self.label1.setText(_("Font size:"))
        self.label2.setText(_("Function &name:"))
        self.label_2.setText(_("&Documentation:"))
        self.label_3.setText(_("Python &code:"))
from calibre.gui2.widgets2 import ColorButton
