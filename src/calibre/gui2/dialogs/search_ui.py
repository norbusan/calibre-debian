# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/search.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(872, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.um_label = QtWidgets.QLabel(self.frame)
        self.um_label.setMinimumSize(QtCore.QSize(150, 0))
        self.um_label.setWordWrap(True)
        self.um_label.setOpenExternalLinks(True)
        self.um_label.setObjectName("um_label")
        self.verticalLayout_3.addWidget(self.um_label)
        self.gridLayout_2.addWidget(self.frame, 0, 2, 3, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.matchkind = QtWidgets.QComboBox(Dialog)
        self.matchkind.setObjectName("matchkind")
        self.matchkind.addItem("")
        self.matchkind.addItem("")
        self.matchkind.addItem("")
        self.gridLayout_2.addWidget(self.matchkind, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.all = QtWidgets.QLineEdit(self.groupBox)
        self.all.setObjectName("all")
        self.horizontalLayout.addWidget(self.all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.phrase = QtWidgets.QLineEdit(self.groupBox)
        self.phrase.setObjectName("phrase")
        self.horizontalLayout_2.addWidget(self.phrase)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.any = QtWidgets.QLineEdit(self.groupBox)
        self.any.setObjectName("any")
        self.horizontalLayout_3.addWidget(self.any)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.none = QtWidgets.QLineEdit(self.groupBox_2)
        self.none.setObjectName("none")
        self.horizontalLayout_4.addWidget(self.none)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.title_box = EnLineEdit(self.tab_2)
        self.title_box.setObjectName("title_box")
        self.gridLayout.addWidget(self.title_box, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.authors_box = EditWithComplete(self.tab_2)
        self.authors_box.setObjectName("authors_box")
        self.gridLayout.addWidget(self.authors_box, 2, 1, 1, 1)
        self.series_box = EditWithComplete(self.tab_2)
        self.series_box.setObjectName("series_box")
        self.gridLayout.addWidget(self.series_box, 3, 1, 1, 1)
        self.tags_box = EditWithComplete(self.tab_2)
        self.tags_box.setObjectName("tags_box")
        self.gridLayout.addWidget(self.tags_box, 4, 1, 1, 1)
        self.general_box = QtWidgets.QLineEdit(self.tab_2)
        self.general_box.setObjectName("general_box")
        self.gridLayout.addWidget(self.general_box, 6, 1, 1, 1)
        self.general_combo = QtWidgets.QComboBox(self.tab_2)
        self.general_combo.setObjectName("general_combo")
        self.gridLayout.addWidget(self.general_combo, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clear_button = QtWidgets.QPushButton(self.tab_2)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.tab_2_button_box = QtWidgets.QDialogButtonBox(self.tab_2)
        self.tab_2_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.tab_2_button_box.setObjectName("tab_2_button_box")
        self.horizontalLayout_6.addWidget(self.tab_2_button_box)
        self.gridLayout.addLayout(self.horizontalLayout_6, 8, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.date_field = QtWidgets.QComboBox(self.tab_3)
        self.date_field.setObjectName("date_field")
        self.horizontalLayout_5.addWidget(self.date_field)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.dateop_date = QtWidgets.QComboBox(self.tab_3)
        self.dateop_date.setObjectName("dateop_date")
        self.horizontalLayout_5.addWidget(self.dateop_date)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sel_date = QtWidgets.QRadioButton(self.tab_3)
        self.sel_date.setText("")
        self.sel_date.setObjectName("sel_date")
        self.horizontalLayout_7.addWidget(self.sel_date)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.date_year = QtWidgets.QSpinBox(self.tab_3)
        self.date_year.setMinimum(102)
        self.date_year.setMaximum(10000)
        self.date_year.setObjectName("date_year")
        self.horizontalLayout_7.addWidget(self.date_year)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.date_month = QtWidgets.QComboBox(self.tab_3)
        self.date_month.setObjectName("date_month")
        self.horizontalLayout_7.addWidget(self.date_month)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.date_day = QtWidgets.QSpinBox(self.tab_3)
        self.date_day.setMaximum(31)
        self.date_day.setObjectName("date_day")
        self.horizontalLayout_7.addWidget(self.date_day)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sel_daysago = QtWidgets.QRadioButton(self.tab_3)
        self.sel_daysago.setText("")
        self.sel_daysago.setObjectName("sel_daysago")
        self.horizontalLayout_8.addWidget(self.sel_daysago)
        self.date_daysago = QtWidgets.QSpinBox(self.tab_3)
        self.date_daysago.setMaximum(999999)
        self.date_daysago.setObjectName("date_daysago")
        self.horizontalLayout_8.addWidget(self.date_daysago)
        self.date_ago_type = QtWidgets.QComboBox(self.tab_3)
        self.date_ago_type.setObjectName("date_ago_type")
        self.horizontalLayout_8.addWidget(self.date_ago_type)
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sel_human = QtWidgets.QRadioButton(self.tab_3)
        self.sel_human.setText("")
        self.sel_human.setObjectName("sel_human")
        self.horizontalLayout_9.addWidget(self.sel_human)
        self.date_human = QtWidgets.QComboBox(self.tab_3)
        self.date_human.setObjectName("date_human")
        self.horizontalLayout_9.addWidget(self.date_human)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.tab_3_button_box = QtWidgets.QDialogButtonBox(self.tab_3)
        self.tab_3_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.tab_3_button_box.setObjectName("tab_3_button_box")
        self.verticalLayout_4.addWidget(self.tab_3_button_box)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.label_5.setBuddy(self.matchkind)
        self.label.setBuddy(self.all)
        self.label_2.setBuddy(self.all)
        self.label_3.setBuddy(self.all)
        self.label_4.setBuddy(self.all)
        self.label_7.setBuddy(self.title_box)
        self.label_8.setBuddy(self.authors_box)
        self.label_9.setBuddy(self.series_box)
        self.label_10.setBuddy(self.tags_box)
        self.label_6.setBuddy(self.date_field)
        self.label_14.setBuddy(self.date_year)
        self.label_15.setBuddy(self.date_month)
        self.label_16.setBuddy(self.date_day)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.tab_3_button_box.accepted.connect(Dialog.accept)
        self.tab_3_button_box.rejected.connect(Dialog.reject)
        self.tab_2_button_box.accepted.connect(Dialog.accept)
        self.tab_2_button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.all, self.phrase)
        Dialog.setTabOrder(self.phrase, self.any)
        Dialog.setTabOrder(self.any, self.none)
        Dialog.setTabOrder(self.none, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.title_box)
        Dialog.setTabOrder(self.title_box, self.authors_box)
        Dialog.setTabOrder(self.authors_box, self.series_box)
        Dialog.setTabOrder(self.series_box, self.tags_box)
        Dialog.setTabOrder(self.tags_box, self.general_combo)
        Dialog.setTabOrder(self.general_combo, self.general_box)
        Dialog.setTabOrder(self.general_box, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.tab_2_button_box)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Advanced Search"))
        self.um_label.setText(_("<p>You can also perform other kinds of advanced searches, for example checking for books that have no covers, combining multiple search expression using Boolean operators and so on. See the <a href=\"%s\">The Search Interface</a> for more information."))
        self.label_5.setText(_("What &kind of match to use:"))
        self.matchkind.setItemText(0, _("Contains: the word or phrase matches anywhere in the metadata field"))
        self.matchkind.setItemText(1, _("Equals: the word or phrase must match the entire metadata field"))
        self.matchkind.setItemText(2, _("Regular expression: the expression must match anywhere in the metadata field"))
        self.groupBox.setTitle(_("Find entries that have..."))
        self.label.setText(_("A&ll these words:"))
        self.label_2.setText(_("&This exact phrase:"))
        self.label_3.setText(_("O&ne or more of these words:"))
        self.groupBox_2.setTitle(_("But don\'t show entries that have..."))
        self.label_4.setText(_("Any of these &unwanted words:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("A&dvanced Search"))
        self.label_7.setText(_("&Title:"))
        self.title_box.setToolTip(_("Enter the title."))
        self.label_8.setText(_("&Author:"))
        self.label_9.setText(_("&Series:"))
        self.label_10.setText(_("Ta&gs:"))
        self.authors_box.setToolTip(_("Enter an author\'s name. Only one author can be used."))
        self.series_box.setToolTip(_("Enter a series name, without an index. Only one series name can be used."))
        self.tags_box.setToolTip(_("Enter tags separated by spaces"))
        self.clear_button.setText(_("&Clear"))
        self.label_11.setText(_("Search only in specific fields:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Titl&e/Author/Series ..."))
        self.label_6.setText(_("&Search the"))
        self.label_13.setText(_("date column for books whose date is "))
        self.label_17.setText(_("..."))
        self.label_14.setText(_("&year"))
        self.label_15.setText(_("mo&nth"))
        self.label_16.setText(_("&day"))
        self.label_18.setText(_(" ago"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("&Date searches"))

from calibre.gui2.complete2 import EditWithComplete
from calibre.gui2.widgets import EnLineEdit

