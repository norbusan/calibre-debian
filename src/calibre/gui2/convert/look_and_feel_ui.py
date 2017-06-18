# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/look_and_feel.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 619)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainTabs = QtWidgets.QTabWidget(Form)
        self.MainTabs.setObjectName("MainTabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.formLayout = QtWidgets.QFormLayout(self.tab1)
        self.formLayout.setObjectName("formLayout")
        self.label_18 = QtWidgets.QLabel(self.tab1)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.opt_base_font_size = QtWidgets.QDoubleSpinBox(self.tab1)
        self.opt_base_font_size.setDecimals(1)
        self.opt_base_font_size.setMinimum(0.0)
        self.opt_base_font_size.setMaximum(50.0)
        self.opt_base_font_size.setSingleStep(1.0)
        self.opt_base_font_size.setProperty("value", 15.0)
        self.opt_base_font_size.setObjectName("opt_base_font_size")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.opt_base_font_size)
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.opt_font_size_mapping = QtWidgets.QLineEdit(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_font_size_mapping.sizePolicy().hasHeightForWidth())
        self.opt_font_size_mapping.setSizePolicy(sizePolicy)
        self.opt_font_size_mapping.setObjectName("opt_font_size_mapping")
        self.horizontalLayout.addWidget(self.opt_font_size_mapping)
        self.button_font_key = QtWidgets.QToolButton(self.tab1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("wizard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_font_key.setIcon(icon)
        self.button_font_key.setIconSize(QtCore.QSize(32, 32))
        self.button_font_key.setObjectName("button_font_key")
        self.horizontalLayout.addWidget(self.button_font_key)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_6 = QtWidgets.QLabel(self.tab1)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.opt_minimum_line_height = QtWidgets.QDoubleSpinBox(self.tab1)
        self.opt_minimum_line_height.setDecimals(1)
        self.opt_minimum_line_height.setMaximum(900.0)
        self.opt_minimum_line_height.setObjectName("opt_minimum_line_height")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.opt_minimum_line_height)
        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.opt_line_height = QtWidgets.QDoubleSpinBox(self.tab1)
        self.opt_line_height.setDecimals(1)
        self.opt_line_height.setObjectName("opt_line_height")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.opt_line_height)
        self.label_10 = QtWidgets.QLabel(self.tab1)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.opt_embed_font_family = FontFamilyChooser(self.tab1)
        self.opt_embed_font_family.setObjectName("opt_embed_font_family")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.opt_embed_font_family)
        self.opt_embed_all_fonts = QtWidgets.QCheckBox(self.tab1)
        self.opt_embed_all_fonts.setObjectName("opt_embed_all_fonts")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.opt_embed_all_fonts)
        self.opt_subset_embedded_fonts = QtWidgets.QCheckBox(self.tab1)
        self.opt_subset_embedded_fonts.setObjectName("opt_subset_embedded_fonts")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.opt_subset_embedded_fonts)
        self.opt_expand_css = QtWidgets.QCheckBox(self.tab1)
        self.opt_expand_css.setObjectName("opt_expand_css")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.opt_expand_css)
        self.opt_keep_ligatures = QtWidgets.QCheckBox(self.tab1)
        self.opt_keep_ligatures.setObjectName("opt_keep_ligatures")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.opt_keep_ligatures)
        self.opt_disable_font_rescaling = QtWidgets.QCheckBox(self.tab1)
        self.opt_disable_font_rescaling.setObjectName("opt_disable_font_rescaling")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.opt_disable_font_rescaling)
        self.MainTabs.addTab(self.tab1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.opt_input_encoding = EncodingComboBox(self.tab)
        self.opt_input_encoding.setEditable(True)
        self.opt_input_encoding.setObjectName("opt_input_encoding")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.opt_input_encoding)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.opt_change_justification = QtWidgets.QComboBox(self.tab)
        self.opt_change_justification.setObjectName("opt_change_justification")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.opt_change_justification)
        self.opt_smarten_punctuation = QtWidgets.QCheckBox(self.tab)
        self.opt_smarten_punctuation.setObjectName("opt_smarten_punctuation")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.opt_smarten_punctuation)
        self.opt_unsmarten_punctuation = QtWidgets.QCheckBox(self.tab)
        self.opt_unsmarten_punctuation.setObjectName("opt_unsmarten_punctuation")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.opt_unsmarten_punctuation)
        self.opt_asciiize = QtWidgets.QCheckBox(self.tab)
        self.opt_asciiize.setObjectName("opt_asciiize")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.opt_asciiize)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.MainTabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.opt_remove_paragraph_spacing_indent_size = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.opt_remove_paragraph_spacing_indent_size.setDecimals(1)
        self.opt_remove_paragraph_spacing_indent_size.setMinimum(-0.1)
        self.opt_remove_paragraph_spacing_indent_size.setSingleStep(0.1)
        self.opt_remove_paragraph_spacing_indent_size.setObjectName("opt_remove_paragraph_spacing_indent_size")
        self.gridLayout.addWidget(self.opt_remove_paragraph_spacing_indent_size, 0, 2, 1, 1)
        self.opt_insert_blank_line = QtWidgets.QCheckBox(self.tab_2)
        self.opt_insert_blank_line.setObjectName("opt_insert_blank_line")
        self.gridLayout.addWidget(self.opt_insert_blank_line, 1, 0, 1, 1)
        self.opt_remove_paragraph_spacing = QtWidgets.QCheckBox(self.tab_2)
        self.opt_remove_paragraph_spacing.setObjectName("opt_remove_paragraph_spacing")
        self.gridLayout.addWidget(self.opt_remove_paragraph_spacing, 0, 0, 1, 1)
        self.opt_insert_blank_line_size = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.opt_insert_blank_line_size.setDecimals(1)
        self.opt_insert_blank_line_size.setObjectName("opt_insert_blank_line_size")
        self.gridLayout.addWidget(self.opt_insert_blank_line_size, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.opt_linearize_tables = QtWidgets.QCheckBox(self.tab_2)
        self.opt_linearize_tables.setObjectName("opt_linearize_tables")
        self.gridLayout.addWidget(self.opt_linearize_tables, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.MainTabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.opt_extra_css = QtWidgets.QPlainTextEdit(self.groupBox)
        self.opt_extra_css.setObjectName("opt_extra_css")
        self.gridLayout_4.addWidget(self.opt_extra_css, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.opt_filter_css = QtWidgets.QGroupBox(self.tab_3)
        self.opt_filter_css.setObjectName("opt_filter_css")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.opt_filter_css)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.opt_filter_css)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filter_css_fonts = QtWidgets.QCheckBox(self.opt_filter_css)
        self.filter_css_fonts.setObjectName("filter_css_fonts")
        self.horizontalLayout_3.addWidget(self.filter_css_fonts)
        self.filter_css_margins = QtWidgets.QCheckBox(self.opt_filter_css)
        self.filter_css_margins.setObjectName("filter_css_margins")
        self.horizontalLayout_3.addWidget(self.filter_css_margins)
        self.filter_css_padding = QtWidgets.QCheckBox(self.opt_filter_css)
        self.filter_css_padding.setObjectName("filter_css_padding")
        self.horizontalLayout_3.addWidget(self.filter_css_padding)
        self.filter_css_floats = QtWidgets.QCheckBox(self.opt_filter_css)
        self.filter_css_floats.setObjectName("filter_css_floats")
        self.horizontalLayout_3.addWidget(self.filter_css_floats)
        self.filter_css_colors = QtWidgets.QCheckBox(self.opt_filter_css)
        self.filter_css_colors.setObjectName("filter_css_colors")
        self.horizontalLayout_3.addWidget(self.filter_css_colors)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.opt_filter_css)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.filter_css_others = QtWidgets.QLineEdit(self.opt_filter_css)
        self.filter_css_others.setObjectName("filter_css_others")
        self.horizontalLayout_4.addWidget(self.filter_css_others)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.opt_filter_css)
        self.MainTabs.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.opt_transform_css_rules = RulesWidget(self.tab_4)
        self.opt_transform_css_rules.setObjectName("opt_transform_css_rules")
        self.verticalLayout_4.addWidget(self.opt_transform_css_rules)
        self.MainTabs.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.MainTabs)
        self.label_18.setBuddy(self.opt_base_font_size)
        self.label_2.setBuddy(self.opt_font_size_mapping)
        self.label_6.setBuddy(self.opt_minimum_line_height)
        self.label.setBuddy(self.opt_line_height)
        self.label_10.setBuddy(self.opt_embed_font_family)
        self.label_5.setBuddy(self.opt_change_justification)
        self.label_3.setBuddy(self.opt_input_encoding)
        self.label_7.setBuddy(self.opt_insert_blank_line_size)
        self.label_4.setBuddy(self.opt_remove_paragraph_spacing_indent_size)
        self.label_9.setBuddy(self.filter_css_others)

        self.retranslateUi(Form)
        self.MainTabs.setCurrentIndex(0)
        self.opt_disable_font_rescaling.toggled['bool'].connect(self.opt_base_font_size.setDisabled)
        self.opt_disable_font_rescaling.toggled['bool'].connect(self.opt_font_size_mapping.setDisabled)
        self.opt_remove_paragraph_spacing.toggled['bool'].connect(self.label_4.setEnabled)
        self.opt_remove_paragraph_spacing.toggled['bool'].connect(self.opt_remove_paragraph_spacing_indent_size.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        self.label_18.setText(_("Base font si&ze:"))
        self.opt_base_font_size.setSuffix(_(" pt"))
        self.label_2.setText(_("Font size &key:"))
        self.button_font_key.setToolTip(_("Wizard to help you choose an appropriate font size key"))
        self.button_font_key.setText(_("..."))
        self.label_6.setText(_("Minim&um line height:"))
        self.opt_minimum_line_height.setSuffix(_(" %"))
        self.label.setText(_("L&ine height:"))
        self.opt_line_height.setSuffix(_(" pt"))
        self.label_10.setText(_("Embed font fami&ly:"))
        self.opt_embed_all_fonts.setText(_("&Embed all fonts in document"))
        self.opt_subset_embedded_fonts.setText(_("&Subset all embedded fonts"))
        self.opt_expand_css.setText(_("E&xpand CSS"))
        self.opt_keep_ligatures.setText(_("Keep &ligatures"))
        self.opt_disable_font_rescaling.setText(_("&Disable font size rescaling"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab1), _("&Fonts"))
        self.label_5.setText(_("Text &justification:"))
        self.opt_smarten_punctuation.setText(_("Smarten &punctuation"))
        self.opt_unsmarten_punctuation.setText(_("&UnSmarten punctuation"))
        self.opt_asciiize.setText(_("&Transliterate unicode characters to ASCII"))
        self.label_3.setText(_("I&nput character encoding:"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab), _("T&ext"))
        self.label_7.setText(_("&Line size:"))
        self.opt_remove_paragraph_spacing_indent_size.setToolTip(_("<p>When calibre removes inter paragraph spacing, it automatically sets a paragraph indent, to ensure that paragraphs can be easily distinguished. This option controls the width of that indent."))
        self.opt_remove_paragraph_spacing_indent_size.setSpecialValueText(_("No change"))
        self.opt_remove_paragraph_spacing_indent_size.setSuffix(_(" em"))
        self.opt_insert_blank_line.setText(_("Insert &blank line between paragraphs"))
        self.opt_remove_paragraph_spacing.setText(_("Remove &spacing between paragraphs"))
        self.opt_insert_blank_line_size.setSuffix(_(" em"))
        self.label_4.setText(_("I&ndent size:"))
        self.opt_linearize_tables.setText(_("&Linearize tables"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab_2), _("&Layout"))
        self.groupBox.setTitle(_("E&xtra CSS"))
        self.opt_filter_css.setTitle(_("Filter Style Information"))
        self.label_8.setText(_("Select what style information you want completely removed:"))
        self.filter_css_fonts.setToolTip(_("Removes the font-family CSS property"))
        self.filter_css_fonts.setText(_("&Fonts"))
        self.filter_css_margins.setToolTip(_("Removes the margin CSS properties. Note that page margins are not affected by this setting."))
        self.filter_css_margins.setText(_("&Margins"))
        self.filter_css_padding.setToolTip(_("Removes the padding CSS properties"))
        self.filter_css_padding.setText(_("&Padding"))
        self.filter_css_floats.setToolTip(_("Convert floating images/text into static images/text"))
        self.filter_css_floats.setText(_("F&loats"))
        self.filter_css_colors.setToolTip(_("Removes foreground and background colors"))
        self.filter_css_colors.setText(_("&Colors"))
        self.label_9.setText(_("Other CSS Propert&ies:"))
        self.filter_css_others.setToolTip(_("Comma separated list of CSS properties to remove. For example: display, color, font-family"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab_3), _("&Styling"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.tab_4), _("&Transform styles"))

from calibre.gui2.css_transform_rules import RulesWidget
from calibre.gui2.font_family_chooser import FontFamilyChooser
from calibre.gui2.widgets import EncodingComboBox

