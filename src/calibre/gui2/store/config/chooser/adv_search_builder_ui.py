# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/store/config/chooser/adv_search_builder.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(752, 472)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(I("search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.sh_label = QtWidgets.QLabel(self.groupBox_2)
        self.sh_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sh_label.setOpenExternalLinks(True)
        self.sh_label.setObjectName("sh_label")
        self.verticalLayout_2.addWidget(self.sh_label)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.name_box = EnLineEdit(self.tab_2)
        self.name_box.setObjectName("name_box")
        self.gridLayout.addWidget(self.name_box, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.price_label = QtWidgets.QLabel(self.tab_2)
        self.price_label.setObjectName("price_label")
        self.gridLayout.addWidget(self.price_label, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clear_button = QtWidgets.QPushButton(self.tab_2)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.tab_2_button_box = QtWidgets.QDialogButtonBox(self.tab_2)
        self.tab_2_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.tab_2_button_box.setObjectName("tab_2_button_box")
        self.horizontalLayout_6.addWidget(self.tab_2_button_box)
        self.gridLayout.addLayout(self.horizontalLayout_6, 9, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.description_box = EnLineEdit(self.tab_2)
        self.description_box.setObjectName("description_box")
        self.gridLayout.addWidget(self.description_box, 2, 1, 1, 1)
        self.format_box = QtWidgets.QLineEdit(self.tab_2)
        self.format_box.setObjectName("format_box")
        self.gridLayout.addWidget(self.format_box, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.headquarters_box = EnLineEdit(self.tab_2)
        self.headquarters_box.setObjectName("headquarters_box")
        self.gridLayout.addWidget(self.headquarters_box, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.enabled_combo = QtWidgets.QComboBox(self.tab_2)
        self.enabled_combo.setObjectName("enabled_combo")
        self.enabled_combo.addItem("")
        self.enabled_combo.setItemText(0, "")
        self.enabled_combo.addItem("")
        self.enabled_combo.addItem("")
        self.gridLayout.addWidget(self.enabled_combo, 5, 1, 1, 1)
        self.drm_combo = QtWidgets.QComboBox(self.tab_2)
        self.drm_combo.setObjectName("drm_combo")
        self.drm_combo.addItem("")
        self.drm_combo.setItemText(0, "")
        self.drm_combo.addItem("")
        self.drm_combo.addItem("")
        self.gridLayout.addWidget(self.drm_combo, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.affiliate_combo = QtWidgets.QComboBox(self.tab_2)
        self.affiliate_combo.setObjectName("affiliate_combo")
        self.affiliate_combo.addItem("")
        self.affiliate_combo.setItemText(0, "")
        self.affiliate_combo.addItem("")
        self.affiliate_combo.addItem("")
        self.gridLayout.addWidget(self.affiliate_combo, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_5.setBuddy(self.matchkind)
        self.label.setBuddy(self.all)
        self.label_2.setBuddy(self.all)
        self.label_3.setBuddy(self.all)
        self.label_4.setBuddy(self.all)
        self.label_7.setBuddy(self.name_box)
        self.label_8.setBuddy(self.description_box)
        self.price_label.setBuddy(self.headquarters_box)
        self.label_10.setBuddy(self.format_box)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.all, self.phrase)
        Dialog.setTabOrder(self.phrase, self.any)
        Dialog.setTabOrder(self.any, self.none)
        Dialog.setTabOrder(self.none, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.name_box)
        Dialog.setTabOrder(self.name_box, self.description_box)
        Dialog.setTabOrder(self.description_box, self.headquarters_box)
        Dialog.setTabOrder(self.headquarters_box, self.format_box)
        Dialog.setTabOrder(self.format_box, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.tab_2_button_box)
        Dialog.setTabOrder(self.tab_2_button_box, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.matchkind)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Advanced Search"))
        self.label_5.setText(_("&What kind of match to use:"))
        self.matchkind.setItemText(0, _("Contains: the word or phrase matches anywhere in the metadata field"))
        self.matchkind.setItemText(1, _("Equals: the word or phrase must match the entire metadata field"))
        self.matchkind.setItemText(2, _("Regular expression: the expression must match anywhere in the metadata field"))
        self.groupBox.setTitle(_("Find entries that have..."))
        self.label.setText(_("&All these words:"))
        self.label_2.setText(_("This exact &phrase:"))
        self.label_3.setText(_("&One or more of these words:"))
        self.groupBox_2.setTitle(_("But don\'t show entries that have..."))
        self.label_4.setText(_("Any of these &unwanted words:"))
        self.sh_label.setText(_("See the <a href=\"%s\">User Manual</a> for more help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("A&dvanced Search"))
        self.label_7.setText(_("&Name:"))
        self.name_box.setToolTip(_("Enter the title."))
        self.label_8.setText(_("&Description:"))
        self.price_label.setText(_("&Headquarters:"))
        self.clear_button.setText(_("&Clear"))
        self.label_11.setText(_("Search only in specific fields:"))
        self.label_10.setText(_("&Format:"))
        self.label_9.setText(_("Enabled:"))
        self.label_12.setText(_("DRM:"))
        self.enabled_combo.setItemText(1, _("true"))
        self.enabled_combo.setItemText(2, _("false"))
        self.drm_combo.setItemText(1, _("true"))
        self.drm_combo.setItemText(2, _("false"))
        self.label_13.setText(_("Affiliate:"))
        self.affiliate_combo.setItemText(1, _("true"))
        self.affiliate_combo.setItemText(2, _("false"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Nam&e/Description ..."))

from calibre.gui2.widgets import EnLineEdit

