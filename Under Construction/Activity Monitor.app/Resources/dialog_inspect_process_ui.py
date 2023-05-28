# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dialog_inspect_process.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InspectProcess(object):
    def setupUi(self, InspectProcess):
        InspectProcess.setObjectName("InspectProcess")
        InspectProcess.resize(893, 553)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(InspectProcess)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.procress_group_id_label = QtWidgets.QLabel(InspectProcess)
        self.procress_group_id_label.setObjectName("procress_group_id_label")
        self.gridLayout.addWidget(self.procress_group_id_label, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.cpu_percent_value = QtWidgets.QLabel(InspectProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpu_percent_value.sizePolicy().hasHeightForWidth())
        self.cpu_percent_value.setSizePolicy(sizePolicy)
        self.cpu_percent_value.setObjectName("cpu_percent_value")
        self.gridLayout.addWidget(self.cpu_percent_value, 2, 1, 1, 1)
        self.parent_process_value = QtWidgets.QLabel(InspectProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parent_process_value.sizePolicy().hasHeightForWidth())
        self.parent_process_value.setSizePolicy(sizePolicy)
        self.parent_process_value.setObjectName("parent_process_value")
        self.gridLayout.addWidget(self.parent_process_value, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(InspectProcess)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.memory_tab = QtWidgets.QWidget()
        self.memory_tab.setObjectName("memory_tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.memory_tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.data_resident_set_size_label = QtWidgets.QLabel(self.memory_tab)
        self.data_resident_set_size_label.setObjectName("data_resident_set_size_label")
        self.gridLayout_2.addWidget(self.data_resident_set_size_label, 4, 0, 1, 1)
        self.text_resitent_set_size_label = QtWidgets.QLabel(self.memory_tab)
        self.text_resitent_set_size_label.setObjectName("text_resitent_set_size_label")
        self.gridLayout_2.addWidget(self.text_resitent_set_size_label, 3, 0, 1, 1)
        self.unique_set_size_label = QtWidgets.QLabel(self.memory_tab)
        self.unique_set_size_label.setObjectName("unique_set_size_label")
        self.gridLayout_2.addWidget(self.unique_set_size_label, 0, 0, 1, 1)
        self.data_resident_set_size_value = QtWidgets.QLabel(self.memory_tab)
        self.data_resident_set_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.data_resident_set_size_value.setObjectName("data_resident_set_size_value")
        self.gridLayout_2.addWidget(self.data_resident_set_size_value, 4, 1, 1, 1)
        self.unique_set_size_value = QtWidgets.QLabel(self.memory_tab)
        self.unique_set_size_value.setToolTip("")
        self.unique_set_size_value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.unique_set_size_value.setObjectName("unique_set_size_value")
        self.gridLayout_2.addWidget(self.unique_set_size_value, 0, 1, 1, 1)
        self.resident_set_size_value = QtWidgets.QLabel(self.memory_tab)
        self.resident_set_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.resident_set_size_value.setObjectName("resident_set_size_value")
        self.gridLayout_2.addWidget(self.resident_set_size_value, 1, 1, 1, 1)
        self.virtual_memory_size_label = QtWidgets.QLabel(self.memory_tab)
        self.virtual_memory_size_label.setObjectName("virtual_memory_size_label")
        self.gridLayout_2.addWidget(self.virtual_memory_size_label, 2, 0, 1, 1)
        self.text_resitent_set_size_value = QtWidgets.QLabel(self.memory_tab)
        self.text_resitent_set_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.text_resitent_set_size_value.setObjectName("text_resitent_set_size_value")
        self.gridLayout_2.addWidget(self.text_resitent_set_size_value, 3, 1, 1, 1)
        self.virtual_memory_size_value = QtWidgets.QLabel(self.memory_tab)
        self.virtual_memory_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.virtual_memory_size_value.setObjectName("virtual_memory_size_value")
        self.gridLayout_2.addWidget(self.virtual_memory_size_value, 2, 1, 1, 1)
        self.resident_set_size_label = QtWidgets.QLabel(self.memory_tab)
        self.resident_set_size_label.setObjectName("resident_set_size_label")
        self.gridLayout_2.addWidget(self.resident_set_size_label, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(20, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.shared_libraries_size_value = QtWidgets.QLabel(self.memory_tab)
        self.shared_libraries_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.shared_libraries_size_value.setObjectName("shared_libraries_size_value")
        self.gridLayout_3.addWidget(self.shared_libraries_size_value, 1, 1, 1, 1)
        self.dirty_pages_number_value = QtWidgets.QLabel(self.memory_tab)
        self.dirty_pages_number_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dirty_pages_number_value.setObjectName("dirty_pages_number_value")
        self.gridLayout_3.addWidget(self.dirty_pages_number_value, 2, 1, 1, 1)
        self.dirty_pages_number_label = QtWidgets.QLabel(self.memory_tab)
        self.dirty_pages_number_label.setObjectName("dirty_pages_number_label")
        self.gridLayout_3.addWidget(self.dirty_pages_number_label, 2, 0, 1, 1)
        self.proportional_set_size_value = QtWidgets.QLabel(self.memory_tab)
        self.proportional_set_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.proportional_set_size_value.setObjectName("proportional_set_size_value")
        self.gridLayout_3.addWidget(self.proportional_set_size_value, 3, 1, 1, 1)
        self.shared_libraries_size_label = QtWidgets.QLabel(self.memory_tab)
        self.shared_libraries_size_label.setObjectName("shared_libraries_size_label")
        self.gridLayout_3.addWidget(self.shared_libraries_size_label, 1, 0, 1, 1)
        self.shared_memory_size_label = QtWidgets.QLabel(self.memory_tab)
        self.shared_memory_size_label.setObjectName("shared_memory_size_label")
        self.gridLayout_3.addWidget(self.shared_memory_size_label, 0, 0, 1, 1)
        self.shared_memory_size_value = QtWidgets.QLabel(self.memory_tab)
        self.shared_memory_size_value.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.shared_memory_size_value.setObjectName("shared_memory_size_value")
        self.gridLayout_3.addWidget(self.shared_memory_size_value, 0, 1, 1, 1)
        self.proportional_set_size_label = QtWidgets.QLabel(self.memory_tab)
        self.proportional_set_size_label.setObjectName("proportional_set_size_label")
        self.gridLayout_3.addWidget(self.proportional_set_size_label, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 5, 0, 1, 1)
        self.swapped_size_label = QtWidgets.QLabel(self.memory_tab)
        self.swapped_size_label.setObjectName("swapped_size_label")
        self.gridLayout_3.addWidget(self.swapped_size_label, 4, 0, 1, 1)
        self.swapped_size_value = QtWidgets.QLabel(self.memory_tab)
        self.swapped_size_value.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.swapped_size_value.setObjectName("swapped_size_value")
        self.gridLayout_3.addWidget(self.swapped_size_value, 4, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.memory_tab, "")
        self.statistics_tab = QtWidgets.QWidget()
        self.statistics_tab.setObjectName("statistics_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.statistics_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.statistics_tab)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.tabWidget.addTab(self.statistics_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 5)
        self.user_label = QtWidgets.QLabel(InspectProcess)
        self.user_label.setObjectName("user_label")
        self.gridLayout.addWidget(self.user_label, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(InspectProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.parent_process_label = QtWidgets.QLabel(InspectProcess)
        self.parent_process_label.setObjectName("parent_process_label")
        self.gridLayout.addWidget(self.parent_process_label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.process_group_id_value = QtWidgets.QLabel(InspectProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_group_id_value.sizePolicy().hasHeightForWidth())
        self.process_group_id_value.setSizePolicy(sizePolicy)
        self.process_group_id_value.setObjectName("process_group_id_value")
        self.gridLayout.addWidget(self.process_group_id_value, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(InspectProcess)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 5)
        self.user_value = QtWidgets.QLabel(InspectProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_value.sizePolicy().hasHeightForWidth())
        self.user_value.setSizePolicy(sizePolicy)
        self.user_value.setObjectName("user_value")
        self.gridLayout.addWidget(self.user_value, 0, 4, 1, 1)
        self.cpu_percent_label = QtWidgets.QLabel(InspectProcess)
        self.cpu_percent_label.setObjectName("cpu_percent_label")
        self.gridLayout.addWidget(self.cpu_percent_label, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_9 = QtWidgets.QLabel(InspectProcess)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(InspectProcess)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InspectProcess)

    def retranslateUi(self, InspectProcess):
        _translate = QtCore.QCoreApplication.translate
        InspectProcess.setWindowTitle(_translate("InspectProcess", "Form"))
        self.procress_group_id_label.setText(_translate("InspectProcess", "Procress Group ID:"))
        self.cpu_percent_value.setText(_translate("InspectProcess", "TextLabel"))
        self.parent_process_value.setText(_translate("InspectProcess", "TextLabel"))
        self.data_resident_set_size_label.setToolTip(_translate("InspectProcess",
                                                                "<html><head/><body><p>The amount of physical memory devoted to other than executable code.</p></body></html>"))
        self.data_resident_set_size_label.setText(_translate("InspectProcess", "Data Resident Set Size:"))
        self.text_resitent_set_size_label.setToolTip(_translate("InspectProcess",
                                                                "<html><head/><body><p>The amount of memory devoted to executable code. </p></body></html>"))
        self.text_resitent_set_size_label.setText(_translate("InspectProcess", "Text Resident Set Size:"))
        self.unique_set_size_label.setToolTip(_translate("InspectProcess",
                                                         "<html><head/><body><p>This is the memory which is unique to a process and which would be freed if the process was terminated right now.</p></body></html>"))
        self.unique_set_size_label.setText(_translate("InspectProcess", "Unique Set Size:"))
        self.data_resident_set_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.unique_set_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.resident_set_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.virtual_memory_size_label.setToolTip(_translate("InspectProcess",
                                                             "<html><head/><body><p>This is the total amount of virtual memory used by the process. </p></body></html>"))
        self.virtual_memory_size_label.setText(_translate("InspectProcess", "Vistual Memory Size:"))
        self.text_resitent_set_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.virtual_memory_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.resident_set_size_label.setToolTip(_translate("InspectProcess",
                                                           "<html><head/><body><p>This is the non-swapped physical memory a process has used. </p></body></html>"))
        self.resident_set_size_label.setText(_translate("InspectProcess", "Resident Set Size:"))
        self.shared_libraries_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.dirty_pages_number_value.setText(_translate("InspectProcess", "TextLabel"))
        self.dirty_pages_number_label.setToolTip(
            _translate("InspectProcess", "<html><head/><body><p>The number of dirty pages.</p></body></html>"))
        self.dirty_pages_number_label.setText(_translate("InspectProcess", "Dirty Pages Number:"))
        self.proportional_set_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.shared_libraries_size_label.setToolTip(_translate("InspectProcess",
                                                               "<html><head/><body><p>The memory used by shared libraries.</p></body></html>"))
        self.shared_libraries_size_label.setText(_translate("InspectProcess", "Shared libraries Size:"))
        self.shared_memory_size_label.setToolTip(_translate("InspectProcess",
                                                            "<html><head/><body><p> Memory that could be potentially shared with other processes.</p></body></html>"))
        self.shared_memory_size_label.setText(_translate("InspectProcess", "Shared Memory Size:"))
        self.shared_memory_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.proportional_set_size_label.setToolTip(_translate("InspectProcess",
                                                               "<html><head/><body><p>The amount of memory shared with other processes, accounted in a way that the amount is divided evenly between the processes that share it. </p></body></html>"))
        self.proportional_set_size_label.setText(_translate("InspectProcess", "Proportional Set Size:"))
        self.swapped_size_label.setToolTip(_translate("InspectProcess",
                                                      "<html><head/><body><p>Amount of memory that has been swapped out to disk.</p></body></html>"))
        self.swapped_size_label.setText(_translate("InspectProcess", "Swapped Size:"))
        self.swapped_size_value.setText(_translate("InspectProcess", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.memory_tab), _translate("InspectProcess", "Memory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statistics_tab),
                                  _translate("InspectProcess", "Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("InspectProcess", "Open Files and Ports"))
        self.user_label.setText(_translate("InspectProcess", "User:"))
        self.label_4.setText(_translate("InspectProcess", "TextLabel"))
        self.parent_process_label.setText(_translate("InspectProcess", "Parent Process:"))
        self.process_group_id_value.setText(_translate("InspectProcess", "TextLabel"))
        self.user_value.setText(_translate("InspectProcess", "TextLabel"))
        self.cpu_percent_label.setText(_translate("InspectProcess", "% CPU:"))
        self.label_9.setText(_translate("InspectProcess", "Recent hangs:"))
