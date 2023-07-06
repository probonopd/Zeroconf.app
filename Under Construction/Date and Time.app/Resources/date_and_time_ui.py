# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date_and_time.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 555)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Date and Time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"        alignment: center;\n"
"        }\n"
"        QTabWidget::pane { /* The tab widget frame */\n"
"        position: absolute;\n"
"        top: -0.9em;\n"
"        }\n"
"       ")
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.DateAndTimeTab = QtWidgets.QWidget()
        self.DateAndTimeTab.setObjectName("DateAndTimeTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DateAndTimeTab)
        self.verticalLayout_3.setContentsMargins(23, 34, 23, 23)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(23)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dat_timeedit_widget = QtWidgets.QTimeEdit(self.DateAndTimeTab)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.dat_timeedit_widget.setFont(font)
        self.dat_timeedit_widget.setWrapping(False)
        self.dat_timeedit_widget.setAccelerated(False)
        self.dat_timeedit_widget.setProperty("showGroupSeparator", False)
        self.dat_timeedit_widget.setCalendarPopup(False)
        self.dat_timeedit_widget.setObjectName("dat_timeedit_widget")
        self.gridLayout_4.addWidget(self.dat_timeedit_widget, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.dat_calendar_widget = QtWidgets.QCalendarWidget(self.DateAndTimeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dat_calendar_widget.sizePolicy().hasHeightForWidth())
        self.dat_calendar_widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.dat_calendar_widget.setFont(font)
        self.dat_calendar_widget.setGridVisible(False)
        self.dat_calendar_widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.dat_calendar_widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.dat_calendar_widget.setNavigationBarVisible(True)
        self.dat_calendar_widget.setDateEditEnabled(True)
        self.dat_calendar_widget.setObjectName("dat_calendar_widget")
        self.gridLayout_4.addWidget(self.dat_calendar_widget, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.dat_clock_widget = AnalogClock(self.DateAndTimeTab)
        self.dat_clock_widget.setMinimumSize(QtCore.QSize(160, 160))
        self.dat_clock_widget.setMaximumSize(QtCore.QSize(600, 600))
        self.dat_clock_widget.setBaseSize(QtCore.QSize(200, 200))
        self.dat_clock_widget.setObjectName("dat_clock_widget")
        self.gridLayout_4.addWidget(self.dat_clock_widget, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 5, 0, 1, 2)
        self.ntp_servers_comboBox = QtWidgets.QComboBox(self.DateAndTimeTab)
        self.ntp_servers_comboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ntp_servers_comboBox.sizePolicy().hasHeightForWidth())
        self.ntp_servers_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.ntp_servers_comboBox.setFont(font)
        self.ntp_servers_comboBox.setObjectName("ntp_servers_comboBox")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.ntp_servers_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.ntp_servers_comboBox, 0, 1, 1, 1)
        self.dat_dateedit_widget = QtWidgets.QDateEdit(self.DateAndTimeTab)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.dat_dateedit_widget.setFont(font)
        self.dat_dateedit_widget.setObjectName("dat_dateedit_widget")
        self.gridLayout_4.addWidget(self.dat_dateedit_widget, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.date_and_time_auto_checkbox = QtWidgets.QCheckBox(self.DateAndTimeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_and_time_auto_checkbox.sizePolicy().hasHeightForWidth())
        self.date_and_time_auto_checkbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.date_and_time_auto_checkbox.setFont(font)
        self.date_and_time_auto_checkbox.setObjectName("date_and_time_auto_checkbox")
        self.gridLayout_4.addWidget(self.date_and_time_auto_checkbox, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(26)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.DateAndTimeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dt_set_custom_format = QtWidgets.QPushButton(self.DateAndTimeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dt_set_custom_format.sizePolicy().hasHeightForWidth())
        self.dt_set_custom_format.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.dt_set_custom_format.setFont(font)
        self.dt_set_custom_format.setObjectName("dt_set_custom_format")
        self.horizontalLayout_2.addWidget(self.dt_set_custom_format)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.DateAndTimeTab, "")
        self.TimeZoneTab = QtWidgets.QWidget()
        self.TimeZoneTab.setObjectName("TimeZoneTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.TimeZoneTab)
        self.verticalLayout_4.setContentsMargins(23, 34, 23, 23)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.TimeZoneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.set_time_zone_automatically_checkbox = QtWidgets.QCheckBox(self.TimeZoneTab)
        self.set_time_zone_automatically_checkbox.setObjectName("set_time_zone_automatically_checkbox")
        self.verticalLayout_4.addWidget(self.set_time_zone_automatically_checkbox, 0, QtCore.Qt.AlignHCenter)
        self.tz_time_zone_world_map_widget = TimeZoneWorldMap(self.TimeZoneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tz_time_zone_world_map_widget.sizePolicy().hasHeightForWidth())
        self.tz_time_zone_world_map_widget.setSizePolicy(sizePolicy)
        self.tz_time_zone_world_map_widget.setMinimumSize(QtCore.QSize(400, 200))
        self.tz_time_zone_world_map_widget.setObjectName("tz_time_zone_world_map_widget")
        self.verticalLayout_4.addWidget(self.tz_time_zone_world_map_widget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(23)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setObjectName("gridLayout")
        self.tz_time_zone_label = QtWidgets.QLabel(self.TimeZoneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tz_time_zone_label.sizePolicy().hasHeightForWidth())
        self.tz_time_zone_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.tz_time_zone_label.setFont(font)
        self.tz_time_zone_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tz_time_zone_label.setObjectName("tz_time_zone_label")
        self.gridLayout.addWidget(self.tz_time_zone_label, 0, 0, 1, 1)
        self.tz_time_zone_value = QtWidgets.QLabel(self.TimeZoneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tz_time_zone_value.sizePolicy().hasHeightForWidth())
        self.tz_time_zone_value.setSizePolicy(sizePolicy)
        self.tz_time_zone_value.setObjectName("tz_time_zone_value")
        self.gridLayout.addWidget(self.tz_time_zone_value, 0, 1, 1, 1)
        self.tz_closest_city_label = QtWidgets.QLabel(self.TimeZoneTab)
        self.tz_closest_city_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tz_closest_city_label.setObjectName("tz_closest_city_label")
        self.gridLayout.addWidget(self.tz_closest_city_label, 1, 0, 1, 1)
        self.tz_closest_city_combobox = QtWidgets.QComboBox(self.TimeZoneTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tz_closest_city_combobox.sizePolicy().hasHeightForWidth())
        self.tz_closest_city_combobox.setSizePolicy(sizePolicy)
        self.tz_closest_city_combobox.setObjectName("tz_closest_city_combobox")
        self.gridLayout.addWidget(self.tz_closest_city_combobox, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.TimeZoneTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(23, 34, 23, 23)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(23, 23, 23, 23)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.dt_use_24h_clock = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.dt_use_24h_clock.setFont(font)
        self.dt_use_24h_clock.setChecked(True)
        self.dt_use_24h_clock.setObjectName("dt_use_24h_clock")
        self.verticalLayout_2.addWidget(self.dt_use_24h_clock)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 13, 0, 0)
        self.horizontalLayout.setSpacing(23)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Sans")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelpAbout = QtWidgets.QAction(MainWindow)
        self.actionHelpAbout.setObjectName("actionHelpAbout")
        self.action_undo = QtWidgets.QAction(MainWindow)
        self.action_undo.setEnabled(False)
        self.action_undo.setObjectName("action_undo")
        self.action_cut = QtWidgets.QAction(MainWindow)
        self.action_cut.setObjectName("action_cut")
        self.action_copy = QtWidgets.QAction(MainWindow)
        self.action_copy.setObjectName("action_copy")
        self.action_paste = QtWidgets.QAction(MainWindow)
        self.action_paste.setObjectName("action_paste")
        self.action_delete = QtWidgets.QAction(MainWindow)
        self.action_delete.setObjectName("action_delete")
        self.action_set_date_and_time_automatically = QtWidgets.QAction(MainWindow)
        self.action_set_date_and_time_automatically.setCheckable(True)
        self.action_set_date_and_time_automatically.setObjectName("action_set_date_and_time_automatically")
        self.action_set_time_zone_automatically = QtWidgets.QAction(MainWindow)
        self.action_set_time_zone_automatically.setCheckable(True)
        self.action_set_time_zone_automatically.setObjectName("action_set_time_zone_automatically")
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.action_undo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_cut)
        self.menuEdit.addAction(self.action_copy)
        self.menuEdit.addAction(self.action_paste)
        self.menuEdit.addAction(self.action_delete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_set_date_and_time_automatically)
        self.menuEdit.addAction(self.action_set_time_zone_automatically)
        self.menuHelp.addAction(self.actionHelpAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.ntp_servers_comboBox.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Date and Time"))
        self.dat_timeedit_widget.setDisplayFormat(_translate("MainWindow", "H:mm:ss AP"))
        self.ntp_servers_comboBox.setItemText(0, _translate("MainWindow", "Africa (africa.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(1, _translate("MainWindow", "Antartica (antarctica.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(2, _translate("MainWindow", "Asia (asia.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(3, _translate("MainWindow", "Europe (europe.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(4, _translate("MainWindow", "Nort America (north-america.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(5, _translate("MainWindow", "Oceania (oceania.pool.ntp.org)"))
        self.ntp_servers_comboBox.setItemText(6, _translate("MainWindow", "South America (south-america.pool.ntp.org)"))
        self.date_and_time_auto_checkbox.setText(_translate("MainWindow", "Set date and time automatically"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; vertical-align:sub;\">To set date and time formats, use International prefrences</span></p></body></html>"))
        self.dt_set_custom_format.setText(_translate("MainWindow", "Open International"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DateAndTimeTab), _translate("MainWindow", "Date and Time"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">To select a time zone, click the map near your location and choose a city from the Closetes City Menu.<br/>You can also the time zone change automatically, if possible, based on your current location.</span></p></body></html>"))
        self.set_time_zone_automatically_checkbox.setText(_translate("MainWindow", "Set time zone automatically using current location"))
        self.tz_time_zone_label.setText(_translate("MainWindow", "Time Zone:"))
        self.tz_time_zone_value.setText(_translate("MainWindow", " "))
        self.tz_closest_city_label.setText(_translate("MainWindow", "Closest City:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TimeZoneTab), _translate("MainWindow", "Time Zone"))
        self.groupBox.setTitle(_translate("MainWindow", "Show the date and time"))
        self.checkBox_2.setText(_translate("MainWindow", "Display the time with seconds"))
        self.checkBox_4.setText(_translate("MainWindow", "Show the day of the week"))
        self.checkBox_3.setText(_translate("MainWindow", "Show AM/PM"))
        self.checkBox_5.setText(_translate("MainWindow", "Flash time separator"))
        self.dt_use_24h_clock.setText(_translate("MainWindow", "Use 24-hour clock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clock"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionHelpAbout.setText(_translate("MainWindow", "About Date and Time"))
        self.action_undo.setText(_translate("MainWindow", "Undo"))
        self.action_undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_cut.setText(_translate("MainWindow", "Cut"))
        self.action_cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_copy.setText(_translate("MainWindow", "Copy"))
        self.action_copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_paste.setText(_translate("MainWindow", "Paste"))
        self.action_paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_delete.setText(_translate("MainWindow", "Delete"))
        self.action_delete.setShortcut(_translate("MainWindow", "Del"))
        self.action_set_date_and_time_automatically.setText(_translate("MainWindow", "Set date and time automatically"))
        self.action_set_time_zone_automatically.setText(_translate("MainWindow", "Set time zone automatically"))
from widget_analogclock import AnalogClock
from widget_timezone_world_map import TimeZoneWorldMap
