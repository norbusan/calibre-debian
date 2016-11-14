# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/scheduler.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 575)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("scheduler.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search = SearchBox2(Dialog)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.go_button = QtWidgets.QToolButton(Dialog)
        self.go_button.setObjectName("go_button")
        self.horizontalLayout_2.addWidget(self.go_button)
        self.clear_search_button = QtWidgets.QToolButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(I("clear_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_search_button.setIcon(icon1)
        self.clear_search_button.setObjectName("clear_search_button")
        self.horizontalLayout_2.addWidget(self.clear_search_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 518, 498))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.detail_box = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.detail_box.setObjectName("detail_box")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.blurb = QtWidgets.QLabel(self.tab)
        self.blurb.setWordWrap(True)
        self.blurb.setOpenExternalLinks(True)
        self.blurb.setObjectName("blurb")
        self.verticalLayout.addWidget(self.blurb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.schedule = QtWidgets.QCheckBox(self.frame)
        self.schedule.setObjectName("schedule")
        self.verticalLayout_2.addWidget(self.schedule)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.days_of_week = QtWidgets.QRadioButton(self.frame)
        self.days_of_week.setObjectName("days_of_week")
        self.horizontalLayout.addWidget(self.days_of_week)
        self.days_of_month = QtWidgets.QRadioButton(self.frame)
        self.days_of_month.setObjectName("days_of_month")
        self.horizontalLayout.addWidget(self.days_of_month)
        self.every_x_days = QtWidgets.QRadioButton(self.frame)
        self.every_x_days.setObjectName("every_x_days")
        self.horizontalLayout.addWidget(self.every_x_days)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.schedule_stack = QtWidgets.QStackedWidget(self.frame)
        self.schedule_stack.setObjectName("schedule_stack")
        self.verticalLayout_2.addWidget(self.schedule_stack)
        self.last_downloaded = QtWidgets.QLabel(self.frame)
        self.last_downloaded.setText("")
        self.last_downloaded.setWordWrap(True)
        self.last_downloaded.setObjectName("last_downloaded")
        self.verticalLayout_2.addWidget(self.last_downloaded)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.account = QtWidgets.QGroupBox(self.tab)
        self.account.setObjectName("account")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.account)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.username = QtWidgets.QLineEdit(self.account)
        self.username.setObjectName("username")
        self.gridLayout_2.addWidget(self.username, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.account)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.account)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.account)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_2.addWidget(self.password, 1, 1, 1, 1)
        self.show_password = QtWidgets.QCheckBox(self.account)
        self.show_password.setObjectName("show_password")
        self.gridLayout_2.addWidget(self.show_password, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.account)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.detail_box.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_title_tag = QtWidgets.QCheckBox(self.tab_2)
        self.add_title_tag.setObjectName("add_title_tag")
        self.gridLayout_3.addWidget(self.add_title_tag, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 2)
        self.keep_issues = QtWidgets.QSpinBox(self.tab_2)
        self.keep_issues.setMaximum(100000)
        self.keep_issues.setObjectName("keep_issues")
        self.gridLayout_3.addWidget(self.keep_issues, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 4, 1, 1, 1)
        self.custom_tags = QtWidgets.QLineEdit(self.tab_2)
        self.custom_tags.setObjectName("custom_tags")
        self.gridLayout_3.addWidget(self.custom_tags, 1, 2, 1, 1)
        self.detail_box.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.detail_box)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 2, 1)
        self.recipes = QtWidgets.QTreeView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recipes.sizePolicy().hasHeightForWidth())
        self.recipes.setSizePolicy(sizePolicy)
        self.recipes.setProperty("showDropIndicator", False)
        self.recipes.setIconSize(QtCore.QSize(16, 16))
        self.recipes.setAnimated(True)
        self.recipes.setHeaderHidden(True)
        self.recipes.setObjectName("recipes")
        self.gridLayout.addWidget(self.recipes, 1, 0, 1, 1)
        self.count_label = QtWidgets.QLabel(Dialog)
        self.count_label.setText("")
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setObjectName("count_label")
        self.gridLayout.addWidget(self.count_label, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.old_news = QtWidgets.QSpinBox(Dialog)
        self.old_news.setMaximum(1000)
        self.old_news.setObjectName("old_news")
        self.horizontalLayout_3.addWidget(self.old_news)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.download_all_button = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(I("news.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_all_button.setIcon(icon2)
        self.download_all_button.setObjectName("download_all_button")
        self.gridLayout.addWidget(self.download_all_button, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.label_2.setBuddy(self.username)
        self.label_3.setBuddy(self.password)
        self.label_5.setBuddy(self.custom_tags)
        self.label_6.setBuddy(self.keep_issues)
        self.label_7.setBuddy(self.old_news)

        self.retranslateUi(Dialog)
        self.detail_box.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.add_title_tag.toggled['bool'].connect(self.keep_issues.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Schedule news download"))
        self.go_button.setText(_("Go"))
        self.blurb.setText(_("blurb"))
        self.schedule.setText(_("&Schedule for download:"))
        self.days_of_week.setText(_("Days of  week"))
        self.days_of_month.setText(_("Days of month"))
        self.every_x_days.setText(_("Every x days"))
        self.account.setTitle(_("&Account"))
        self.label_2.setText(_("&Username:"))
        self.label_3.setText(_("&Password:"))
        self.show_password.setText(_("&Show password"))
        self.label.setText(_("For the scheduling to work, you must leave calibre running."))
        self.detail_box.setTabText(self.detail_box.indexOf(self.tab), _("&Schedule"))
        self.add_title_tag.setText(_("Add &title as tag"))
        self.label_5.setText(_("&Extra  tags:"))
        self.label_6.setToolTip(_("Maximum number of copies (issues) of this recipe to keep.  Set to 0 to keep all (disable)."))
        self.label_6.setText(_("&Keep at most:"))
        self.keep_issues.setToolTip(_("<p>When set, this option will cause calibre to keep, at most, the specified number of issues of this periodical. Every time a new issue is downloaded, the oldest one is deleted, if the total is larger than this number.\n"
"<p>Note that this feature only works if you have the option to add the title as tag checked, above.\n"
"<p>Also, the setting for deleting periodicals older than a number of days, below, takes priority over this setting."))
        self.keep_issues.setSpecialValueText(_("all issues"))
        self.keep_issues.setSuffix(_(" issues"))
        self.detail_box.setTabText(self.detail_box.indexOf(self.tab_2), _("&Advanced"))
        self.label_7.setText(_("Delete downloaded news &older than:"))
        self.old_news.setToolTip(_("<p>Delete downloaded news older than the specified number of days. Set to zero to disable.\n"
"<p>You can also control the maximum number of issues of a specific periodical that are kept by clicking the Advanced tab for that periodical above."))
        self.old_news.setSpecialValueText(_("never delete"))
        self.old_news.setSuffix(_(" days"))
        self.download_all_button.setToolTip(_("Download all scheduled news sources at once"))
        self.download_all_button.setText(_("Download &all scheduled"))

from calibre.gui2.search_box import SearchBox2

