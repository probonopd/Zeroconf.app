# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dialog_send_signal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendSignalDialog(object):
    def setupUi(self, SendSignalDialog):
        SendSignalDialog.setObjectName("SendSignalDialog")
        SendSignalDialog.setWindowModality(QtCore.Qt.NonModal)
        SendSignalDialog.setEnabled(True)
        SendSignalDialog.resize(465, 133)
        SendSignalDialog.setWindowTitle(" ")
        SendSignalDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SendSignalDialog)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainVbox = QtWidgets.QVBoxLayout()
        self.MainVbox.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.MainVbox.setContentsMargins(0, 0, 0, 0)
        self.MainVbox.setSpacing(6)
        self.MainVbox.setObjectName("MainVbox")
        self.Label = QtWidgets.QLabel(SendSignalDialog)
        self.Label.setObjectName("Label")
        self.MainVbox.addWidget(self.Label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SignalListComboBox = QtWidgets.QComboBox(SendSignalDialog)
        self.SignalListComboBox.setObjectName("SignalListComboBox")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.SignalListComboBox.addItem("")
        self.MainVbox.addWidget(self.SignalListComboBox, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.MainVbox.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CancelButton = QtWidgets.QPushButton(SendSignalDialog)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.SendButton = QtWidgets.QPushButton(SendSignalDialog)
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout.addWidget(self.SendButton)
        self.MainVbox.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.MainVbox)

        self.retranslateUi(SendSignalDialog)
        self.CancelButton.clicked.connect(SendSignalDialog.reject) # type: ignore
        self.SendButton.clicked.connect(SendSignalDialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SendSignalDialog)

    def retranslateUi(self, SendSignalDialog):
        _translate = QtCore.QCoreApplication.translate
        self.Label.setText(_translate("SendSignalDialog", "Please select a signal to send to the process \'%s\'"))
        self.SignalListComboBox.setItemText(0, _translate("SendSignalDialog", "Hangup (SIGHUP)"))
        self.SignalListComboBox.setItemText(1, _translate("SendSignalDialog", "Interrupt (SIGINT)"))
        self.SignalListComboBox.setItemText(2, _translate("SendSignalDialog", "Quit (SIGQUIT)"))
        self.SignalListComboBox.setItemText(3, _translate("SendSignalDialog", "Abort (SIGABRT)"))
        self.SignalListComboBox.setItemText(4, _translate("SendSignalDialog", "Kill (SIGKILL)"))
        self.SignalListComboBox.setItemText(5, _translate("SendSignalDialog", "Alarm (SIGALRM)"))
        self.SignalListComboBox.setItemText(6, _translate("SendSignalDialog", "User Defined 1 (SIGUSR1)"))
        self.SignalListComboBox.setItemText(7, _translate("SendSignalDialog", "User Defined 2 (SIGUSR2)"))
        self.CancelButton.setText(_translate("SendSignalDialog", "Cancel"))
        self.SendButton.setText(_translate("SendSignalDialog", "Send"))
