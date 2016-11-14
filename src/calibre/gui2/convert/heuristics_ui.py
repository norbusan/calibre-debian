# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/heuristics.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 470)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.help_label = QtWidgets.QLabel(Form)
        self.help_label.setWordWrap(True)
        self.help_label.setOpenExternalLinks(True)
        self.help_label.setObjectName("help_label")
        self.verticalLayout.addWidget(self.help_label)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.opt_enable_heuristics = QtWidgets.QCheckBox(Form)
        self.opt_enable_heuristics.setObjectName("opt_enable_heuristics")
        self.verticalLayout.addWidget(self.opt_enable_heuristics)
        self.heuristic_options = QtWidgets.QGroupBox(Form)
        self.heuristic_options.setObjectName("heuristic_options")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.heuristic_options)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.opt_unwrap_lines = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_unwrap_lines.setObjectName("opt_unwrap_lines")
        self.verticalLayout_2.addWidget(self.opt_unwrap_lines)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.huf_label = QtWidgets.QLabel(self.heuristic_options)
        self.huf_label.setObjectName("huf_label")
        self.horizontalLayout.addWidget(self.huf_label)
        self.opt_html_unwrap_factor = QtWidgets.QDoubleSpinBox(self.heuristic_options)
        self.opt_html_unwrap_factor.setToolTip("")
        self.opt_html_unwrap_factor.setMaximum(1.0)
        self.opt_html_unwrap_factor.setSingleStep(0.05)
        self.opt_html_unwrap_factor.setProperty("value", 0.4)
        self.opt_html_unwrap_factor.setObjectName("opt_html_unwrap_factor")
        self.horizontalLayout.addWidget(self.opt_html_unwrap_factor)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.opt_markup_chapter_headings = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_markup_chapter_headings.setObjectName("opt_markup_chapter_headings")
        self.verticalLayout_2.addWidget(self.opt_markup_chapter_headings)
        self.opt_renumber_headings = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_renumber_headings.setObjectName("opt_renumber_headings")
        self.verticalLayout_2.addWidget(self.opt_renumber_headings)
        self.opt_delete_blank_paragraphs = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_delete_blank_paragraphs.setObjectName("opt_delete_blank_paragraphs")
        self.verticalLayout_2.addWidget(self.opt_delete_blank_paragraphs)
        self.opt_format_scene_breaks = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_format_scene_breaks.setObjectName("opt_format_scene_breaks")
        self.verticalLayout_2.addWidget(self.opt_format_scene_breaks)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.heuristic_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.opt_replace_scene_breaks = QtWidgets.QComboBox(self.heuristic_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_replace_scene_breaks.sizePolicy().hasHeightForWidth())
        self.opt_replace_scene_breaks.setSizePolicy(sizePolicy)
        self.opt_replace_scene_breaks.setEditable(True)
        self.opt_replace_scene_breaks.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.opt_replace_scene_breaks.setObjectName("opt_replace_scene_breaks")
        self.horizontalLayout_2.addWidget(self.opt_replace_scene_breaks)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.opt_dehyphenate = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_dehyphenate.setObjectName("opt_dehyphenate")
        self.verticalLayout_2.addWidget(self.opt_dehyphenate)
        self.opt_italicize_common_cases = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_italicize_common_cases.setObjectName("opt_italicize_common_cases")
        self.verticalLayout_2.addWidget(self.opt_italicize_common_cases)
        self.opt_fix_indents = QtWidgets.QCheckBox(self.heuristic_options)
        self.opt_fix_indents.setObjectName("opt_fix_indents")
        self.verticalLayout_2.addWidget(self.opt_fix_indents)
        spacerItem3 = QtWidgets.QSpacerItem(131, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.heuristic_options)
        self.huf_label.setBuddy(self.opt_html_unwrap_factor)
        self.label_2.setBuddy(self.opt_replace_scene_breaks)

        self.retranslateUi(Form)
        self.opt_enable_heuristics.toggled['bool'].connect(self.opt_html_unwrap_factor.setEnabled)
        self.opt_enable_heuristics.toggled['bool'].connect(self.huf_label.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.help_label.setText(_("<b>Heuristic processing</b> means that calibre will scan your book for common patterns and fix them. As the name implies, this involves guesswork, which means that it could end up worsening the result of a conversion, if calibre guesses wrong. Therefore, it is disabled by default. Often, if a conversion does not turn out as you expect, turning on heuristics can improve matters. Read more about the various heuristic processing options in the <a href=\"%s\">User Manual</a>."))
        self.opt_enable_heuristics.setText(_("Enable &heuristic processing"))
        self.heuristic_options.setTitle(_("Heuristic Processing"))
        self.opt_unwrap_lines.setText(_("Unwrap lines"))
        self.huf_label.setText(_("Line &un-wrap factor:"))
        self.opt_markup_chapter_headings.setText(_("Detect and markup unformatted chapter headings and sub headings"))
        self.opt_renumber_headings.setText(_("Renumber sequences of <h1> or <h2> tags to prevent splitting"))
        self.opt_delete_blank_paragraphs.setText(_("Delete blank lines between paragraphs"))
        self.opt_format_scene_breaks.setText(_("Ensure scene breaks are consistently formatted"))
        self.label_2.setText(_("Replace soft scene &breaks:"))
        self.opt_dehyphenate.setText(_("Remove unnecessary hyphens"))
        self.opt_italicize_common_cases.setText(_("Italicize common words and patterns"))
        self.opt_fix_indents.setText(_("Replace entity indents with CSS indents"))

