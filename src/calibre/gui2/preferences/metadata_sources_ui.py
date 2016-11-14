# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/metadata_sources.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 439)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stack = QtWidgets.QStackedWidget(Form)
        self.stack.setObjectName("stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.opt_find_first_edition_date = QtWidgets.QCheckBox(self.page)
        self.opt_find_first_edition_date.setObjectName("opt_find_first_edition_date")
        self.gridLayout.addWidget(self.opt_find_first_edition_date, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
        self.opt_wait_after_first_cover_result = QtWidgets.QSpinBox(self.page)
        self.opt_wait_after_first_cover_result.setObjectName("opt_wait_after_first_cover_result")
        self.gridLayout.addWidget(self.opt_wait_after_first_cover_result, 9, 2, 1, 1)
        self.opt_fewer_tags = QtWidgets.QCheckBox(self.page)
        self.opt_fewer_tags.setObjectName("opt_fewer_tags")
        self.gridLayout.addWidget(self.opt_fewer_tags, 5, 1, 1, 2)
        self.opt_swap_author_names = QtWidgets.QCheckBox(self.page)
        self.opt_swap_author_names.setObjectName("opt_swap_author_names")
        self.gridLayout.addWidget(self.opt_swap_author_names, 2, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fields_view = QtWidgets.QListView(self.groupBox_2)
        self.fields_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.fields_view.setObjectName("fields_view")
        self.gridLayout_2.addWidget(self.fields_view, 0, 0, 1, 2)
        self.select_all_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_all_button.setObjectName("select_all_button")
        self.gridLayout_2.addWidget(self.select_all_button, 1, 0, 1, 1)
        self.clear_all_button = QtWidgets.QPushButton(self.groupBox_2)
        self.clear_all_button.setObjectName("clear_all_button")
        self.gridLayout_2.addWidget(self.clear_all_button, 1, 1, 1, 1)
        self.select_default_button = QtWidgets.QPushButton(self.groupBox_2)
        self.select_default_button.setObjectName("select_default_button")
        self.gridLayout_2.addWidget(self.select_default_button, 2, 0, 1, 1)
        self.set_as_default_button = QtWidgets.QPushButton(self.groupBox_2)
        self.set_as_default_button.setObjectName("set_as_default_button")
        self.gridLayout_2.addWidget(self.set_as_default_button, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 2)
        self.opt_txt_comments = QtWidgets.QCheckBox(self.page)
        self.opt_txt_comments.setObjectName("opt_txt_comments")
        self.gridLayout.addWidget(self.opt_txt_comments, 1, 1, 1, 2)
        self.opt_max_tags = QtWidgets.QSpinBox(self.page)
        self.opt_max_tags.setObjectName("opt_max_tags")
        self.gridLayout.addWidget(self.opt_max_tags, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)
        self.opt_wait_after_first_identify_result = QtWidgets.QSpinBox(self.page)
        self.opt_wait_after_first_identify_result.setObjectName("opt_wait_after_first_identify_result")
        self.gridLayout.addWidget(self.opt_wait_after_first_identify_result, 8, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.sources_view = QtWidgets.QTableView(self.groupBox)
        self.sources_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sources_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sources_view.setObjectName("sources_view")
        self.verticalLayout_3.addWidget(self.sources_view)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.configure_plugin_button = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("plugins.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.configure_plugin_button.setIcon(icon)
        self.configure_plugin_button.setObjectName("configure_plugin_button")
        self.verticalLayout_3.addWidget(self.configure_plugin_button)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 10, 1)
        self.opt_append_comments = QtWidgets.QCheckBox(self.page)
        self.opt_append_comments.setObjectName("opt_append_comments")
        self.gridLayout.addWidget(self.opt_append_comments, 4, 1, 1, 1)
        self.tag_map_rules_button = QtWidgets.QPushButton(self.page)
        self.tag_map_rules_button.setObjectName("tag_map_rules_button")
        self.gridLayout.addWidget(self.tag_map_rules_button, 6, 1, 1, 2)
        self.stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stack.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stack)
        self.label_3.setBuddy(self.opt_wait_after_first_identify_result)
        self.label_4.setBuddy(self.opt_wait_after_first_cover_result)
        self.label_2.setBuddy(self.opt_max_tags)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.opt_find_first_edition_date.setText(_("Use published date of \"first edition\" (from worldcat.org)"))
        self.label_3.setText(_("Max. &time to wait after first match is found:"))
        self.label_4.setText(_("Max. time to wait after first &cover is found:"))
        self.opt_wait_after_first_cover_result.setSuffix(_(" secs"))
        self.opt_fewer_tags.setToolTip(_("<p>Different metadata sources have different sets of tags for the same book. If this option is checked, then calibre will use the smaller tag sets. These tend to be more like genres, while the larger tag sets tend to describe the books content.\n"
"<p>Note that this option will only make a practical difference if one of the metadata sources has a genre like tag set for the book you are searching for. Most often, they all have large tag sets."))
        self.opt_fewer_tags.setStatusTip(_("Prefer smaller tag sets when picking tags from different metadata sources"))
        self.opt_fewer_tags.setText(_("Prefer &fewer tags"))
        self.opt_swap_author_names.setText(_("Swap author names from FN LN to LN, FN"))
        self.groupBox_2.setTitle(_("Downloaded metadata fields"))
        self.fields_view.setToolTip(_("If you uncheck any fields, metadata for those fields will not be downloaded"))
        self.select_all_button.setText(_("&Select all"))
        self.clear_all_button.setText(_("&Clear all"))
        self.select_default_button.setToolTip(_("Restore your own subset of checked fields that you define using the \'Set as default\' button"))
        self.select_default_button.setText(_("&Select default"))
        self.set_as_default_button.setToolTip(_("Store the currently checked fields as a default you can restore using the \'Select default\' button"))
        self.set_as_default_button.setText(_("&Set as default"))
        self.opt_txt_comments.setText(_("Convert all downloaded comments to plain &text"))
        self.label_2.setText(_("Max. &number of tags to download:"))
        self.opt_wait_after_first_identify_result.setSuffix(_(" secs"))
        self.groupBox.setTitle(_("Metadata sources"))
        self.label.setText(_("Disable any metadata sources you do not want by unchecking them. You can also set the cover priority. Covers from sources that have a higher (smaller) priority will be preferred when bulk downloading metadata.\n"
""))
        self.label_5.setText(_("Sources with a red X next to their names must be configured before they will be used. "))
        self.configure_plugin_button.setText(_("Configure selected source"))
        self.opt_append_comments.setToolTip(_("<p>When downloading comments, append the downloaded comments to any existing comment, instead of overwriting them."))
        self.opt_append_comments.setStatusTip(_("When downloading comments, append the downloaded comments to any existing comment, instead of overwriting them."))
        self.opt_append_comments.setText(_("Append &comments to existing"))
        self.tag_map_rules_button.setText(_("Create &rules to filter/transform tags"))


