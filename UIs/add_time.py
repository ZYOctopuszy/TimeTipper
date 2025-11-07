# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_time.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QPushButton,
    QTimeEdit,
)


class UiForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(168, 70)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.timeEdit = QTimeEdit(Form)
        self.timeEdit.setObjectName("timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 1, 0, 1, 1)

        self.sure = QPushButton(Form)
        self.sure.setObjectName("sure")

        self.gridLayout.addWidget(self.sure, 2, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.sure.setText(QCoreApplication.translate("Form", "\u786e\u8ba4", None))

    # retranslateUi
