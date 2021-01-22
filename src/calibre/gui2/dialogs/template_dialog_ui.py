# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/template_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.scroll_area = QtWidgets.QScrollArea(TemplateDialog)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.wid1 = QtWidgets.QWidget()
        self.wid1.setObjectName("wid1")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.wid1)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.color_layout = QtWidgets.QWidget(self.wid1)
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
        self.verticalLayout1.addWidget(self.color_layout)
        self.icon_layout = QtWidgets.QWidget(self.wid1)
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
        self.verticalLayout1.addWidget(self.icon_layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.template_name_label = QtWidgets.QLabel(self.wid1)
        self.template_name_label.setObjectName("template_name_label")
        self.gridLayout.addWidget(self.template_name_label, 0, 0, 1, 1)
        self.template_name = QtWidgets.QComboBox(self.wid1)
        self.template_name.setEditable(True)
        self.template_name.setObjectName("template_name")
        self.gridLayout.addWidget(self.template_name, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.wid1)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.textbox = QtWidgets.QPlainTextEdit(self.wid1)
        self.textbox.setObjectName("textbox")
        self.gridLayout.addWidget(self.textbox, 1, 1, 1, 1)
        self.new_doc_label = QtWidgets.QLabel(self.wid1)
        self.new_doc_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.new_doc_label.setObjectName("new_doc_label")
        self.gridLayout.addWidget(self.new_doc_label, 3, 0, 1, 1)
        self.new_doc = QtWidgets.QTextEdit(self.wid1)
        self.new_doc.setObjectName("new_doc")
        self.gridLayout.addWidget(self.new_doc, 3, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.wid1)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 5, 0, 1, 1)
        self.template_value = QtWidgets.QLineEdit(self.wid1)
        self.template_value.setReadOnly(True)
        self.template_value.setObjectName("template_value")
        self.gridLayout.addWidget(self.template_value, 5, 1, 1, 1)
        self.user_label_1 = QtWidgets.QLabel(self.wid1)
        self.user_label_1.setVisible(False)
        self.user_label_1.setObjectName("user_label_1")
        self.gridLayout.addWidget(self.user_label_1, 11, 0, 1, 1)
        self.user_layout_1 = BoxLayout()
        self.user_layout_1.setObjectName("user_layout_1")
        self.gridLayout.addLayout(self.user_layout_1, 11, 1, 1, 1)
        self.user_label_2 = QtWidgets.QLabel(self.wid1)
        self.user_label_2.setVisible(False)
        self.user_label_2.setObjectName("user_label_2")
        self.gridLayout.addWidget(self.user_label_2, 12, 0, 1, 1)
        self.user_layout_2 = BoxLayout()
        self.user_layout_2.setObjectName("user_layout_2")
        self.gridLayout.addLayout(self.user_layout_2, 12, 1, 1, 1)
        self.user_label_3 = QtWidgets.QLabel(self.wid1)
        self.user_label_3.setVisible(False)
        self.user_label_3.setObjectName("user_label_3")
        self.gridLayout.addWidget(self.user_label_3, 13, 0, 1, 1)
        self.user_layout_3 = BoxLayout()
        self.user_layout_3.setObjectName("user_layout_3")
        self.gridLayout.addLayout(self.user_layout_3, 13, 1, 1, 1)
        self.user_label_4 = QtWidgets.QLabel(self.wid1)
        self.user_label_4.setVisible(False)
        self.user_label_4.setObjectName("user_label_4")
        self.gridLayout.addWidget(self.user_label_4, 14, 0, 1, 1)
        self.user_layout_4 = BoxLayout()
        self.user_layout_4.setObjectName("user_layout_4")
        self.gridLayout.addLayout(self.user_layout_4, 14, 1, 1, 1)
        self.user_label_5 = QtWidgets.QLabel(self.wid1)
        self.user_label_5.setVisible(False)
        self.user_label_5.setObjectName("user_label_5")
        self.gridLayout.addWidget(self.user_label_5, 15, 0, 1, 1)
        self.user_layout_5 = BoxLayout()
        self.user_layout_5.setObjectName("user_layout_5")
        self.gridLayout.addLayout(self.user_layout_5, 15, 1, 1, 1)
        self.user_label_6 = QtWidgets.QLabel(self.wid1)
        self.user_label_6.setVisible(False)
        self.user_label_6.setObjectName("user_label_6")
        self.gridLayout.addWidget(self.user_label_6, 16, 0, 1, 1)
        self.user_layout_6 = BoxLayout()
        self.user_layout_6.setObjectName("user_layout_6")
        self.gridLayout.addLayout(self.user_layout_6, 16, 1, 1, 1)
        self.user_label_7 = QtWidgets.QLabel(self.wid1)
        self.user_label_7.setVisible(False)
        self.user_label_7.setObjectName("user_label_7")
        self.gridLayout.addWidget(self.user_label_7, 17, 0, 1, 1)
        self.user_layout_7 = BoxLayout()
        self.user_layout_7.setObjectName("user_layout_7")
        self.gridLayout.addLayout(self.user_layout_7, 17, 1, 1, 1)
        self.user_label_8 = QtWidgets.QLabel(self.wid1)
        self.user_label_8.setVisible(False)
        self.user_label_8.setObjectName("user_label_8")
        self.gridLayout.addWidget(self.user_label_8, 18, 0, 1, 1)
        self.user_layout_8 = BoxLayout()
        self.user_layout_8.setObjectName("user_layout_8")
        self.gridLayout.addLayout(self.user_layout_8, 18, 1, 1, 1)
        self.user_label_9 = QtWidgets.QLabel(self.wid1)
        self.user_label_9.setVisible(False)
        self.user_label_9.setObjectName("user_label_9")
        self.gridLayout.addWidget(self.user_label_9, 19, 0, 1, 1)
        self.user_layout_9 = BoxLayout()
        self.user_layout_9.setObjectName("user_layout_9")
        self.gridLayout.addLayout(self.user_layout_9, 19, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.wid1)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 20, 0, 1, 1)
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.font_size_box = QtWidgets.QSpinBox(self.wid1)
        self.font_size_box.setObjectName("font_size_box")
        self.gridLayout1.addWidget(self.font_size_box, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout1.addItem(spacerItem, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.wid1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout1.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 20, 1, 1, 3)
        self.frame = QtWidgets.QFrame(self.wid1)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 21, 0, 1, 5)
        self.label3 = QtWidgets.QLabel(self.wid1)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 22, 0, 1, 2)
        self.label4 = QtWidgets.QLabel(self.wid1)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 23, 0, 1, 1)
        self.function = QtWidgets.QComboBox(self.wid1)
        self.function.setObjectName("function")
        self.gridLayout.addWidget(self.function, 23, 1, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.wid1)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 24, 0, 1, 1)
        self.func_type = QtWidgets.QLineEdit(self.wid1)
        self.func_type.setReadOnly(True)
        self.func_type.setObjectName("func_type")
        self.gridLayout.addWidget(self.func_type, 24, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.wid1)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 25, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.wid1)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 26, 0, 1, 1)
        self.documentation = QtWidgets.QPlainTextEdit(self.wid1)
        self.documentation.setMaximumSize(QtCore.QSize(16777215, 75))
        self.documentation.setObjectName("documentation")
        self.gridLayout.addWidget(self.documentation, 25, 1, 1, 3)
        self.source_code = QtWidgets.QPlainTextEdit(self.wid1)
        self.source_code.setMaximumSize(QtCore.QSize(16777215, 75))
        self.source_code.setObjectName("source_code")
        self.gridLayout.addWidget(self.source_code, 26, 1, 1, 3)
        self.template_tutorial = QtWidgets.QLabel(self.wid1)
        self.template_tutorial.setOpenExternalLinks(True)
        self.template_tutorial.setObjectName("template_tutorial")
        self.gridLayout.addWidget(self.template_tutorial, 27, 1, 1, 1)
        self.template_func_reference = QtWidgets.QLabel(self.wid1)
        self.template_func_reference.setOpenExternalLinks(True)
        self.template_func_reference.setObjectName("template_func_reference")
        self.gridLayout.addWidget(self.template_func_reference, 28, 1, 1, 1)
        self.verticalLayout1.addLayout(self.gridLayout)
        self.scroll_area.setWidget(self.wid1)
        self.verticalLayout.addWidget(self.scroll_area)
        self.colored_field_label.setBuddy(self.colored_field)
        self.color_chooser_label.setBuddy(self.color_name)
        self.icon_chooser_label.setBuddy(self.icon_field)
        self.image_chooser_label.setBuddy(self.color_name)
        self.template_name_label.setBuddy(self.template_name)
        self.label.setBuddy(self.textbox)
        self.new_doc_label.setBuddy(self.new_doc)
        self.label1.setBuddy(self.template_value)
        self.user_label_1.setBuddy(self.template_value)
        self.user_label_2.setBuddy(self.template_value)
        self.user_label_3.setBuddy(self.template_value)
        self.user_label_4.setBuddy(self.template_value)
        self.user_label_5.setBuddy(self.template_value)
        self.user_label_6.setBuddy(self.template_value)
        self.user_label_7.setBuddy(self.template_value)
        self.user_label_8.setBuddy(self.template_value)
        self.user_label_9.setBuddy(self.template_value)
        self.label3.setBuddy(self.function)
        self.label4.setBuddy(self.function)
        self.label_22.setBuddy(self.func_type)
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
        self.template_name_label.setText(_("Template &name:"))
        self.template_name.setToolTip(_("The name of the callable template"))
        self.label.setText(_("T&emplate:"))
        self.textbox.setToolTip(_("The template program text"))
        self.new_doc_label.setText(_("D&ocumentation:"))
        self.new_doc.setToolTip(_("Documentation for the function being defined or edited"))
        self.label1.setText(_("Template value:"))
        self.label1.setToolTip(_("The value of the template using the current book in the library view"))
        self.user_label_1.setText(_("User label"))
        self.user_label_2.setText(_("User label"))
        self.user_label_3.setText(_("User label"))
        self.user_label_4.setText(_("User label"))
        self.user_label_5.setText(_("User label"))
        self.user_label_6.setText(_("User label"))
        self.user_label_7.setText(_("User label"))
        self.user_label_8.setText(_("User label"))
        self.user_label_9.setText(_("User label"))
        self.label2.setText(_("Font size:"))
        self.label3.setText(_("Template Function Reference"))
        self.label4.setText(_("Function &name:"))
        self.label_22.setText(_("&Function type:"))
        self.label_2.setText(_("&Documentation:"))
        self.label_3.setText(_("&Code:"))
from calibre.gui2.dialogs.template_dialog_box_layout import BoxLayout
from calibre.gui2.widgets2 import ColorButton
