# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/server.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 563)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.opt_username = QtWidgets.QLineEdit(Form)
        self.opt_username.setObjectName("opt_username")
        self.gridLayout_5.addWidget(self.opt_username, 1, 1, 1, 2)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)
        self.opt_password = QtWidgets.QLineEdit(Form)
        self.opt_password.setObjectName("opt_password")
        self.gridLayout_5.addWidget(self.opt_password, 2, 1, 1, 1)
        self.opt_max_cover = QtWidgets.QLineEdit(Form)
        self.opt_max_cover.setText("")
        self.opt_max_cover.setObjectName("opt_max_cover")
        self.gridLayout_5.addWidget(self.opt_max_cover, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.opt_port = QtWidgets.QSpinBox(Form)
        self.opt_port.setMaximum(65535)
        self.opt_port.setProperty("value", 8080)
        self.opt_port.setObjectName("opt_port")
        self.gridLayout_5.addWidget(self.opt_port, 0, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.show_server_password = QtWidgets.QCheckBox(Form)
        self.show_server_password.setObjectName("show_server_password")
        self.gridLayout_5.addWidget(self.show_server_password, 3, 1, 1, 2)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 5, 0, 1, 1)
        self.opt_max_opds_items = QtWidgets.QSpinBox(Form)
        self.opt_max_opds_items.setMinimum(10)
        self.opt_max_opds_items.setMaximum(10000)
        self.opt_max_opds_items.setObjectName("opt_max_opds_items")
        self.gridLayout_5.addWidget(self.opt_max_opds_items, 5, 1, 1, 2)
        self.opt_max_opds_ungrouped_items = QtWidgets.QSpinBox(Form)
        self.opt_max_opds_ungrouped_items.setMinimum(25)
        self.opt_max_opds_ungrouped_items.setMaximum(1000000)
        self.opt_max_opds_ungrouped_items.setObjectName("opt_max_opds_ungrouped_items")
        self.gridLayout_5.addWidget(self.opt_max_opds_ungrouped_items, 6, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 6, 0, 1, 1)
        self.label_164 = QtWidgets.QLabel(Form)
        self.label_164.setObjectName("label_164")
        self.gridLayout_5.addWidget(self.label_164, 7, 0, 1, 1)
        self.opt_cs_virtual_lib_on_startup = QtWidgets.QComboBox(Form)
        self.opt_cs_virtual_lib_on_startup.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.opt_cs_virtual_lib_on_startup.setMinimumContentsLength(20)
        self.opt_cs_virtual_lib_on_startup.setObjectName("opt_cs_virtual_lib_on_startup")
        self.gridLayout_5.addWidget(self.opt_cs_virtual_lib_on_startup, 7, 1, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {color:red}")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 8, 0, 1, 1)
        self.opt_url_prefix = QtWidgets.QLineEdit(Form)
        self.opt_url_prefix.setObjectName("opt_url_prefix")
        self.gridLayout_5.addWidget(self.opt_url_prefix, 8, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(Form)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(Form)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_2.addWidget(self.stop_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.test_button = QtWidgets.QPushButton(Form)
        self.test_button.setObjectName("test_button")
        self.horizontalLayout_2.addWidget(self.test_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.opt_autolaunch_server = QtWidgets.QCheckBox(Form)
        self.opt_autolaunch_server.setObjectName("opt_autolaunch_server")
        self.verticalLayout.addWidget(self.opt_autolaunch_server)
        self.view_logs = QtWidgets.QPushButton(Form)
        self.view_logs.setObjectName("view_logs")
        self.verticalLayout.addWidget(self.view_logs)
        spacerItem1 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setWordWrap(True)
        self.label_13.setOpenExternalLinks(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        spacerItem2 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_12.setBuddy(self.opt_password)
        self.label_3.setBuddy(self.opt_max_cover)
        self.label_10.setBuddy(self.opt_port)
        self.label_11.setBuddy(self.opt_username)
        self.label_15.setBuddy(self.opt_max_opds_items)
        self.label_16.setBuddy(self.opt_max_opds_ungrouped_items)
        self.label_2.setBuddy(self.opt_url_prefix)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.label_12.setText(_("&Password:"))
        self.opt_password.setToolTip(_("<p>If you leave the password blank, anyone will be able to\n"
" access your book collection using the web interface.\n"
"<br>\n"
"<p>Some devices have browsers that do not support authentication. If you are having trouble downloading files from the content server, try removing the password."))
        self.opt_max_cover.setToolTip(_("The maximum size (widthxheight) for displayed covers. Larger covers are resized. "))
        self.label_3.setText(_("Max. &cover size:"))
        self.label_10.setText(_("Server &port:"))
        self.label_11.setText(_("&Username:"))
        self.show_server_password.setText(_("&Show password"))
        self.label_15.setText(_("Max. &OPDS items per query:"))
        self.label_16.setText(_("Max. &ungrouped items:"))
        self.label_164.setText(_("Virtual library to apply:"))
        self.opt_cs_virtual_lib_on_startup.setToolTip(_("Setting a virtual library will restrict the books the content server makes available to those in the library. This setting is per library (i.e. you can have a different value per library)."))
        self.label.setToolTip(_("<p>Some devices have browsers that do not support authentication. If you are having trouble downloading files from the content server, trying removing the password."))
        self.label.setText(_("Passwords are incompatible with some devices"))
        self.label_2.setText(_("&URL Prefix:"))
        self.opt_url_prefix.setToolTip(_("A prefix that is applied to all URLs in the content server. Useful only if you plan to put the server behind another server like Apache, with a reverse proxy."))
        self.start_button.setText(_("&Start Server"))
        self.stop_button.setText(_("St&op Server"))
        self.test_button.setText(_("&Test Server"))
        self.label_9.setText(_("calibre contains a network server that allows you to access your book collection using a browser from anywhere in the world. Any changes to the settings will only take effect after a server restart."))
        self.opt_autolaunch_server.setText(_("Run server &automatically when calibre starts"))
        self.view_logs.setText(_("View &server logs"))
        self.label_13.setText(_("<p>Remember to leave calibre running as the server only runs as long as calibre is running. If you wish to run the server as a standalone entity, please refer to the <a href=\"https://manual.calibre-ebook.com/generated/en/calibre-server.html\">command-line documentation</a>.\n"
"<p>To connect to the calibre server from your device you should use a URL of the form <b>http://myhostname:8080</b>. Here myhostname should be either the fully qualified hostname or the IP address of the computer calibre is running on. If you want to access the server from anywhere in the world, you will have to setup port forwarding for it on your router."))

