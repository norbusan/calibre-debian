# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/adding.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1035, 547)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.opt_read_file_metadata = QtWidgets.QCheckBox(self.tab)
        self.opt_read_file_metadata.setToolTip("")
        self.opt_read_file_metadata.setObjectName("opt_read_file_metadata")
        self.verticalLayout.addWidget(self.opt_read_file_metadata)
        self.opt_swap_author_names = QtWidgets.QCheckBox(self.tab)
        self.opt_swap_author_names.setObjectName("opt_swap_author_names")
        self.verticalLayout.addWidget(self.opt_swap_author_names)
        self.metadata_box = QtWidgets.QGroupBox(self.tab)
        self.metadata_box.setMinimumSize(QtCore.QSize(0, 100))
        self.metadata_box.setObjectName("metadata_box")
        self.verticalLayout.addWidget(self.metadata_box)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.actions_tab = QtWidgets.QWidget()
        self.actions_tab.setObjectName("actions_tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.actions_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.opt_mark_new_books = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_mark_new_books.setObjectName("opt_mark_new_books")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.opt_mark_new_books)
        self.line_2 = QtWidgets.QFrame(self.actions_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.opt_preserve_date_on_ctl = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_preserve_date_on_ctl.setObjectName("opt_preserve_date_on_ctl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.opt_preserve_date_on_ctl)
        self.opt_check_for_dupes_on_ctl = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_check_for_dupes_on_ctl.setObjectName("opt_check_for_dupes_on_ctl")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.opt_check_for_dupes_on_ctl)
        self.line = QtWidgets.QFrame(self.actions_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.opt_manual_add_auto_convert = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_manual_add_auto_convert.setObjectName("opt_manual_add_auto_convert")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.opt_manual_add_auto_convert)
        self.opt_auto_convert_same_fmt = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_auto_convert_same_fmt.setObjectName("opt_auto_convert_same_fmt")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.opt_auto_convert_same_fmt)
        self.line_3 = QtWidgets.QFrame(self.actions_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.opt_add_formats_to_existing = QtWidgets.QCheckBox(self.actions_tab)
        self.opt_add_formats_to_existing.setObjectName("opt_add_formats_to_existing")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.opt_add_formats_to_existing)
        self.opt_automerge = QtWidgets.QComboBox(self.actions_tab)
        self.opt_automerge.setObjectName("opt_automerge")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.opt_automerge)
        self.line_6 = QtWidgets.QFrame(self.actions_tab)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.line_6)
        self.line_4 = QtWidgets.QFrame(self.actions_tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.label_230 = QtWidgets.QLabel(self.actions_tab)
        self.label_230.setObjectName("label_230")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_230)
        self.opt_new_book_tags = QtWidgets.QLineEdit(self.actions_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_new_book_tags.sizePolicy().hasHeightForWidth())
        self.opt_new_book_tags.setSizePolicy(sizePolicy)
        self.opt_new_book_tags.setObjectName("opt_new_book_tags")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.opt_new_book_tags)
        self.line_7 = QtWidgets.QFrame(self.actions_tab)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.line_7)
        self.line_8 = QtWidgets.QFrame(self.actions_tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.line_8)
        self.label_5 = QtWidgets.QLabel(self.actions_tab)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tag_map_rules_button = QtWidgets.QPushButton(self.actions_tab)
        self.tag_map_rules_button.setObjectName("tag_map_rules_button")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.tag_map_rules_button)
        self.line_5 = QtWidgets.QFrame(self.actions_tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.line_5)
        self.label_6 = QtWidgets.QLabel(self.actions_tab)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.add_filter_rules_button = QtWidgets.QPushButton(self.actions_tab)
        self.add_filter_rules_button.setObjectName("add_filter_rules_button")
        self.formLayout_2.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.add_filter_rules_button)
        self.label_7 = QtWidgets.QLabel(self.actions_tab)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.author_map_rules_button = QtWidgets.QPushButton(self.actions_tab)
        self.author_map_rules_button.setObjectName("author_map_rules_button")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.author_map_rules_button)
        self.tabWidget.addTab(self.actions_tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.opt_auto_add_everything = QtWidgets.QCheckBox(self.tab_4)
        self.opt_auto_add_everything.setObjectName("opt_auto_add_everything")
        self.gridLayout_3.addWidget(self.opt_auto_add_everything, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.opt_auto_add_path = HistoryLineEdit(self.tab_4)
        self.opt_auto_add_path.setClearButtonEnabled(True)
        self.opt_auto_add_path.setObjectName("opt_auto_add_path")
        self.horizontalLayout_2.addWidget(self.opt_auto_add_path)
        self.auto_add_browse_button = QtWidgets.QToolButton(self.tab_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("document_open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auto_add_browse_button.setIcon(icon)
        self.auto_add_browse_button.setObjectName("auto_add_browse_button")
        self.horizontalLayout_2.addWidget(self.auto_add_browse_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.opt_auto_add_auto_convert = QtWidgets.QCheckBox(self.tab_4)
        self.opt_auto_add_auto_convert.setObjectName("opt_auto_add_auto_convert")
        self.gridLayout_3.addWidget(self.opt_auto_add_auto_convert, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 7, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.opt_blocked_auto_formats = QtWidgets.QListWidget(self.groupBox)
        self.opt_blocked_auto_formats.setAlternatingRowColors(True)
        self.opt_blocked_auto_formats.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.opt_blocked_auto_formats.setObjectName("opt_blocked_auto_formats")
        self.verticalLayout_2.addWidget(self.opt_blocked_auto_formats)
        self.gridLayout_3.addWidget(self.groupBox, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 2)
        self.opt_auto_add_check_for_duplicates = QtWidgets.QCheckBox(self.tab_4)
        self.opt_auto_add_check_for_duplicates.setObjectName("opt_auto_add_check_for_duplicates")
        self.gridLayout_3.addWidget(self.opt_auto_add_check_for_duplicates, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label_230.setBuddy(self.opt_new_book_tags)
        self.label_5.setBuddy(self.tag_map_rules_button)
        self.label_6.setBuddy(self.add_filter_rules_button)
        self.label_7.setBuddy(self.author_map_rules_button)
        self.label_3.setBuddy(self.opt_blocked_auto_formats)
        self.label.setBuddy(self.opt_auto_add_path)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.opt_add_formats_to_existing.toggled['bool'].connect(self.opt_automerge.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label_4.setText(_("Here you can control how calibre will read metadata from the files you add to it. calibre can either read metadata from the contents of the file, or from the filename."))
        self.opt_read_file_metadata.setText(_("Read &metadata from file contents rather than file name"))
        self.opt_swap_author_names.setToolTip(_("Swap the firstname and lastname of the author. This affects only metadata read from file names."))
        self.opt_swap_author_names.setText(_("&Swap author firstname and lastname when reading author from filename"))
        self.metadata_box.setTitle(_("Configure metadata from file name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Reading &metadata"))
        self.opt_mark_new_books.setText(_("&Mark newly added books"))
        self.opt_preserve_date_on_ctl.setText(_("When using the  \"&Copy to library\" action to copy books between libraries, preserve the date"))
        self.opt_check_for_dupes_on_ctl.setText(_("When using the \"Copy to library\" action check for &duplicates with the same title, author and language"))
        self.opt_manual_add_auto_convert.setText(_("Automatically &convert added books to the preferred output format"))
        self.opt_auto_convert_same_fmt.setToolTip(_("This will force an automatic conversion even if the file being added is the same format as the output format. For example, if you set your output format to EPUB and add an EPUB file, an EPUB to EPUB conversion will be run."))
        self.opt_auto_convert_same_fmt.setText(_("When auto-converting, convert even if the format being added is the &same as the output format"))
        self.opt_add_formats_to_existing.setToolTip(_("Auto-merge: If books with similar titles and authors found, merge the incoming formats automatically into\n"
"existing book records. The box to the right controls what happens when an existing record already has\n"
"the incoming format. Note that this option also affects the Copy to library action.\n"
"\n"
"Title match ignores leading indefinite articles (\"the\", \"a\", \"an\"), punctuation, case, etc. Author match is exact."))
        self.opt_add_formats_to_existing.setText(_("&Auto-merge added books if they already exist:"))
        self.opt_automerge.setToolTip(_("Auto-merge: If books with similar titles and authors found, merge the incoming formats automatically into\n"
"existing book records. This box controls what happens when an existing record already has\n"
"the incoming format:\n"
"\n"
"Ignore duplicate incoming files - means that existing files in your calibre library will not be replaced\n"
"Overwrite existing duplicate files - means that existing files in your calibre library will be replaced\n"
"Create new record for each duplicate file - means that a new book entry will be created for each duplicate file\n"
"\n"
"Title matching ignores leading indefinite articles (\"the\", \"a\", \"an\"), punctuation, case, etc.\n"
"Author matching is exact."))
        self.label_230.setText(_("&Tags to apply when adding a book:"))
        self.opt_new_book_tags.setToolTip(_("A comma-separated list of tags that will be applied to books added to the library"))
        self.label_5.setText(_("Contro&l how tags are processed:"))
        self.tag_map_rules_button.setToolTip(_("Create rules that can filter or transform tags on added books automatically as soon as they are added. "))
        self.tag_map_rules_button.setText(_("&Rules to filter tags read from metadata"))
        self.label_6.setText(_("Control which files are added during bul&k imports:"))
        self.add_filter_rules_button.setToolTip(_("<p>You can specify rules to add/ignore files here. These will be used when recursively adding books from directories."))
        self.add_filter_rules_button.setText(_("Rules to filter added &files"))
        self.label_7.setText(_("Control how auth&ors are processed:"))
        self.author_map_rules_button.setText(_("Rules to manipulate a&uthor names"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actions_tab), _("Adding &actions"))
        self.opt_auto_add_everything.setToolTip(_("By default, calibre will automatically add only known e-book files. \n"
"This option tells calibre to add all file types, except those\n"
"that have been explicitly ignored below."))
        self.opt_auto_add_everything.setText(_("Automatically add files of &all types (not just e-books)"))
        self.opt_auto_add_path.setPlaceholderText(_("Folder to automatically add files from"))
        self.auto_add_browse_button.setToolTip(_("Browse for folder"))
        self.auto_add_browse_button.setText(_("..."))
        self.opt_auto_add_auto_convert.setText(_("Automatically &convert added files to the preferred output format"))
        self.label_3.setText(_("<b>Ignore</b> files with the following &extensions when automatically adding "))
        self.label.setText(_("Specify a &folder. Any files you put into this folder will be automatically added to calibre (restart required)."))
        self.label_2.setText(_("<b>WARNING:</b> Files in the above folder will be deleted after being added to calibre."))
        self.opt_auto_add_check_for_duplicates.setToolTip(_("If set, this option will cause calibre to check if a file\n"
" being automatically added is already in the calibre library.\n"
" If it is, a message will pop up asking you whether\n"
" you want to add it anyway."))
        self.opt_auto_add_check_for_duplicates.setText(_("Check for &duplicates when automatically adding files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _("&Automatic adding"))
from calibre.gui2.widgets import HistoryLineEdit

