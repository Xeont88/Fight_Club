# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Fight_Club_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 373)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_atack_head = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_atack_head.setObjectName("radioButton_atack_head")
        self.verticalLayout.addWidget(self.radioButton_atack_head)
        self.radioButton_atack_torso = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_atack_torso.setObjectName("radioButton_atack_torso")
        self.verticalLayout.addWidget(self.radioButton_atack_torso)
        self.radioButton_atack_belt = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_atack_belt.setObjectName("radioButton_atack_belt")
        self.verticalLayout.addWidget(self.radioButton_atack_belt)
        self.radioButton_atack_legs = QtWidgets.QRadioButton(self.groupbox)
        self.radioButton_atack_legs.setObjectName("radioButton_atack_legs")
        self.verticalLayout.addWidget(self.radioButton_atack_legs)
        self.verticalLayout_3.addWidget(self.groupbox)
        self.verticalLayout_3.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.groupbox1 = QtWidgets.QGroupBox(Form)
        self.groupbox1.setObjectName("groupbox1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupbox1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_def_head = QtWidgets.QRadioButton(self.groupbox1)
        self.radioButton_def_head.setObjectName("radioButton_def_head")
        self.verticalLayout_2.addWidget(self.radioButton_def_head)
        self.radioButton_def_torso = QtWidgets.QRadioButton(self.groupbox1)
        self.radioButton_def_torso.setObjectName("radioButton_def_torso")
        self.verticalLayout_2.addWidget(self.radioButton_def_torso)
        self.radioButton_def_belt = QtWidgets.QRadioButton(self.groupbox1)
        self.radioButton_def_belt.setObjectName("radioButton_def_belt")
        self.verticalLayout_2.addWidget(self.radioButton_def_belt)
        self.radioButton_def_legs = QtWidgets.QRadioButton(self.groupbox1)
        self.radioButton_def_legs.setObjectName("radioButton_def_legs")
        self.verticalLayout_2.addWidget(self.radioButton_def_legs)
        self.verticalLayout_4.addWidget(self.groupbox1)
        self.verticalLayout_4.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_5.addWidget(self.progressBar_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/atack_on_titans_levi_.jpg\"/></p></body></html>"))
        self.label.setText(_translate("Form", "Удар"))
        self.radioButton_atack_head.setText(_translate("Form", "Голова"))
        self.radioButton_atack_torso.setText(_translate("Form", "Торс"))
        self.radioButton_atack_belt.setText(_translate("Form", "Пояс"))
        self.radioButton_atack_legs.setText(_translate("Form", "Ноги"))
        self.label_2.setText(_translate("Form", "Защита"))
        self.radioButton_def_head.setText(_translate("Form", "Голова"))
        self.radioButton_def_torso.setText(_translate("Form", "Торс"))
        self.radioButton_def_belt.setText(_translate("Form", "Пояс"))
        self.radioButton_def_legs.setText(_translate("Form", "Ноги"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/zeke.jpg\"/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Ход!"))
import fc_rc
