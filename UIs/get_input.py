# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_input.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QGridLayout, QLineEdit, QSizePolicy)


# noinspection PyMissingOrEmptyDocstring, PyPep8Naming
class UiGetInput(object):
    def setupUi(self, get_input):
        if not get_input.objectName():
            get_input.setObjectName(u"get_input")
        get_input.resize(344, 39)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(get_input.sizePolicy().hasHeightForWidth())
        get_input.setSizePolicy(sizePolicy)
        get_input.setMinimumSize(QSize(190, 39))
        get_input.setMaximumSize(QSize(16777215, 39))
        icon = QIcon()
        icon.addFile(u"../icons/active.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        get_input.setWindowIcon(icon)
        self.gridLayout = QGridLayout(get_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.get_exe_name = QLineEdit(get_input)
        self.get_exe_name.setObjectName(u"get_exe_name")
        self.get_exe_name.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.get_exe_name, 0, 0, 1, 1)

        self.retranslateUi(get_input)

        QMetaObject.connectSlotsByName(get_input)

    # setupUi

    def retranslateUi(self, get_input):
        get_input.setWindowTitle(QCoreApplication.translate("get_input", u"\u6dfb\u52a0\u5f85\u6740\u6587\u4ef6", None))
        self.get_exe_name.setPlaceholderText(QCoreApplication.translate("get_input",
                                                                        u"\u8bf7\u8f93\u5165\u53ef\u6267\u884c\u6587\u4ef6\u540d(\u542b\u540e\u7f00)",
                                                                        None))
    # retranslateUi
