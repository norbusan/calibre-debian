# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/quickview.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Quickview(object):
    def setupUi(self, Quickview):
        Quickview.setObjectName("Quickview")
        Quickview.resize(768, 342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Quickview.sizePolicy().hasHeightForWidth())
        Quickview.setSizePolicy(sizePolicy)
        self.main_grid_layout = QtWidgets.QGridLayout(Quickview)
        self.main_grid_layout.setObjectName("main_grid_layout")
        self.items_label = QtWidgets.QLabel(Quickview)
        self.items_label.setObjectName("items_label")
        self.main_grid_layout.addWidget(self.items_label, 0, 0, 1, 1)
        self.items = QtWidgets.QListWidget(Quickview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items.sizePolicy().hasHeightForWidth())
        self.items.setSizePolicy(sizePolicy)
        self.items.setObjectName("items")
        self.main_grid_layout.addWidget(self.items, 1, 0, 1, 1)
        self.books_label = QtWidgets.QLabel(Quickview)
        self.books_label.setObjectName("books_label")
        self.main_grid_layout.addWidget(self.books_label, 0, 1, 1, 1)
        self.books_table = QtWidgets.QTableWidget(Quickview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_table.sizePolicy().hasHeightForWidth())
        self.books_table.setSizePolicy(sizePolicy)
        self.books_table.setColumnCount(0)
        self.books_table.setRowCount(0)
        self.books_table.setObjectName("books_table")
        self.main_grid_layout.addWidget(self.books_table, 1, 1, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.lock_qv = QtWidgets.QCheckBox(Quickview)
        self.lock_qv.setObjectName("lock_qv")
        self.hboxlayout.addWidget(self.lock_qv)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.dock_button = QtWidgets.QPushButton(Quickview)
        self.dock_button.setAutoDefault(False)
        self.dock_button.setObjectName("dock_button")
        self.hboxlayout.addWidget(self.dock_button)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.search_button = QtWidgets.QPushButton(Quickview)
        self.search_button.setAutoDefault(False)
        self.search_button.setObjectName("search_button")
        self.hboxlayout.addWidget(self.search_button)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.refresh_button = QtWidgets.QPushButton(Quickview)
        self.refresh_button.setAutoDefault(False)
        self.refresh_button.setObjectName("refresh_button")
        self.hboxlayout.addWidget(self.refresh_button)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem4)
        self.close_button = QtWidgets.QPushButton(Quickview)
        self.close_button.setAutoDefault(False)
        self.close_button.setObjectName("close_button")
        self.hboxlayout.addWidget(self.close_button)
        spacerItem5 = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem5)
        self.main_grid_layout.addLayout(self.hboxlayout, 3, 0, 1, 2)
        self.items_label.setBuddy(self.items)
        self.books_label.setBuddy(self.books_table)

        self.retranslateUi(Quickview)

    def retranslateUi(self, Quickview):

        Quickview.setWindowTitle(_("Quickview"))
        self.lock_qv.setText(_("&Lock Quickview contents"))
        self.lock_qv.setToolTip(_("<p>Select to prevent Quickview from changing content when the\n"
"        selection on the library view is changed</p>"))
        self.dock_button.setText(_("&Dock"))
        self.search_button.setText(_("&Search"))
        self.search_button.setToolTip(_("Search in the library view for the currently highlighted selection"))
        self.refresh_button.setText(_("&Refresh"))
        self.refresh_button.setToolTip(_("When Quickview is locked, refresh the window using the last selected book and that book\'s value in the last selected column."))
        self.close_button.setText(_("&Close"))
